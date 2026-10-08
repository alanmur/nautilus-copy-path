#!/usr/bin/env bash
set -e

TARGET_FILE="${HOME}/.local/share/nautilus-python/extensions/copy-path.py"

if [ -f "${TARGET_FILE}" ]; then
    rm -f "${TARGET_FILE}"
    echo "Removed ${TARGET_FILE}"
fi

if command -v nautilus >/dev/null 2>&1; then
    nautilus -q || true
fi

echo "Uninstalled copy-path extension."
