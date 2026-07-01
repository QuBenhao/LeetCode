/**
 * Environment configuration loader for TypeScript tests.
 * Provides centralized access to PROBLEM_FOLDER and other env vars.
 */
import * as dotenv from 'dotenv';
import * as fs from 'fs';
import * as path from 'path';

let _loaded = false;

export function initEnv(): void {
    if (_loaded) return;
    dotenv.config();
    _loaded = true;
}

export function getProblemFolder(): string {
    initEnv();
    const folder = process.env.PROBLEM_FOLDER;
    return folder && folder.length > 0 ? folder : 'problems';
}

export function getEnv(key: string, defaultValue: string = ''): string {
    initEnv();
    const val = process.env[key];
    return val && val.length > 0 ? val : defaultValue;
}
