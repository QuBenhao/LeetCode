use std::sync::mpsc;
use std::{panic, thread};
use std::time::Duration;

pub fn panic_after<T, F>(d: Duration, f: F) -> T
where
    T: Send + 'static,
    F: FnOnce() -> T,
    F: Send + 'static,
{
    let (done_tx, done_rx) = mpsc::channel();
    let handle = thread::spawn(move || {
        let val = f();
        done_tx.send(()).expect("Unable to send completion signal");
        val
    });

    match done_rx.recv_timeout(d) {
        Ok(_) => handle.join().expect("Thread panicked"),
        Err(_) => {
            if let Err(panic) = handle.join() {
                            panic::resume_unwind(panic);
            } else {
                panic!("Thread took too long")
            }
        },
    }
}