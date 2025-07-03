import argparse
import json
import re
import sys
import traceback
from datetime import datetime, timedelta
from pathlib import Path

from bs4 import BeautifulSoup

__text = """国务院办公厅关于2025年
部分节假日安排的通知
国办发明电〔2024〕12号

各省、自治区、直辖市人民政府，国务院各部委、各直属机构：
经党中央、国务院批准，根据2024年11月修订的《全国年节及纪念日放假办法》，自2025年1月1日起，全体公民放假的假日增加2天，其中春节、劳动节各增加1天。据此对放假调休原则作进一步优化完善，除个别特殊情形外，春节自农历除夕起放假调休8天，国庆节自10月1日起放假调休7天，劳动节放假调休5天，元旦、清明节、端午节、中秋节分别放假调休或连休3天（如逢周三则只在当日放假），国庆节放假如逢中秋节则合并放假8天。
按照上述原则，现将2025年元旦、春节、清明节、劳动节、端午节、中秋节和国庆节放假调休日期的具体安排通知如下。
一、元旦：1月1日（周三）放假1天，不调休。
二、春节：1月28日（农历除夕、周二）至2月4日（农历正月初七、周二）放假调休，共8天。1月26日（周日）、2月8日（周六）上班。
三、清明节：4月4日（周五）至6日（周日）放假，共3天。
四、劳动节：5月1日（周四）至5日（周一）放假调休，共5天。4月27日（周日）上班。
五、端午节：5月31日（周六）至6月2日（周一）放假，共3天。
六、国庆节、中秋节：10月1日（周三）至8日（周三）放假调休，共8天。9月28日（周日）、10月11日（周六）上班。
节假日期间，各地区、各部门要妥善安排好值班和安全、保卫、疫情防控等工作，遇有重大突发事件，要按规定及时报告并妥善处置，确保人民群众祥和平安度过节日假期。
国务院办公厅
2024年11月12日"""


def extract_holidays():
    lines = __text.split('\n')
    year = re.search(r'(\d{4})年', lines[0]).group(1)
    holidays = []
    workdays = []
    for line in lines:
        holiday_match = re.search(r'(\d{1,2}月\d{1,2}日)（.*?）?至((\d{1,2}月)?\d{1,2}日)（.*?）?放假', line)
        if holiday_match:
            start_date_str = holiday_match.group(1)
            end_date_str = holiday_match.group(2)
            start_date = datetime.strptime(f"{year} {start_date_str}", "%Y %m月%d日")
            if "月" not in end_date_str:
                end_date = start_date.replace(day=int(end_date_str[:-1]))
            else:
                end_date = datetime.strptime(f"{year} {end_date_str}", "%Y %m月%d日")
            while start_date <= end_date:
                holidays.append(start_date.strftime("%Y%m%d"))
                start_date += timedelta(days=1)
        else:
            # signal holiday
            holiday_match = re.search(r'(\d{1,2}月\d{1,2}日)（.*?）?放假', line)
            if holiday_match:
                start_date_str = holiday_match.group(1)
                start_date = datetime.strptime(f"{year} {start_date_str}", "%Y %m月%d日")
                holidays.append(start_date.strftime("%Y%m%d"))
            else:
                continue
        if "调休" in line:
            # workdays appear each day
            workday_str = line.split("。")[1].split("上班")[0]
            for wd in workday_str.split("、"):
                wd = wd.split("（")[0].strip()
                if wd:
                    workday_date = datetime.strptime(f"{year} {wd}", "%Y %m月%d日")
                    workdays.append(workday_date.strftime("%Y%m%d"))

    return year, holidays, workdays


def save_holidays_to_json(year, holidays, workdays, file_path: Path):
    # Create the directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if file_path.exists():
        with file_path.open('r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}
    data[year] = {
        "holidays": holidays,
        "workdays": workdays
    }

    # Save the holidays to a JSON file
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def holiday_main(args):
    result = extract_holidays()
    # file_path = "../../data/holiday.json"
    file_path = Path(__file__).parent.parent / "data" / "holidays.json"
    save_holidays_to_json(*result, file_path)


# extract problems from the HTML content
def extract_problems(html_content):
    problems = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for li in soup.find_all('li'):
        a_tag = li.find('a')
        if not a_tag:
            continue
        title = a_tag.text
        url = a_tag['href']
        if "/problems/" not in url:
            continue
        problems.append((title, url))
    return problems


def extract_problems_main(args):
    try:
        with Path(args.source).open('r', encoding='utf-8') as f:
            source = f.read()
        problems = extract_problems(source)
        problem_ids = []
        for title, url in problems:
            problem_id = ".".join(title.rsplit(".")[:-1])
            print(f"Problem ID: {problem_id}, Title: {title}, URL: {url}")
            problem_ids.append(problem_id)
        print(",".join(map(lambda x: f"\"{x}\"", problem_ids)))
    except FileNotFoundError:
        print(f"File not found: {args.source}")
    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spider script")
    sub_parsers = parser.add_subparsers()
    holiday_parser = sub_parsers.add_parser("holiday", help="Extract holidays from the text")
    holiday_parser.add_argument("-p", "--path", type=str, help="Path to the holiday JSON file",
                                default="../../data/holiday.json")
    holiday_parser.set_defaults(func=holiday_main)
    problems_parser = sub_parsers.add_parser("problems", help="Extract problems from the HTML")
    problems_parser.add_argument("-s", "--source", type=str, help="Path to the HTML source file",
                                 default="../../data/source.html")
    problems_parser.set_defaults(func=extract_problems_main)
    _args = parser.parse_args()
    if hasattr(_args, "func"):
        _args.func(_args)
    else:
        parser.print_help()
    sys.exit()
