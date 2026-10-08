#!/usr/bin/env bash
set -e

DEST_DIR="${HOME}/.local/share/nautilus-python/extensions"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_FILE="${SCRIPT_DIR}/extension/copy_path.py"
TARGET_FILE="${DEST_DIR}/copy-path.py"

mkdir -p "${DEST_DIR}"
cp "${SOURCE_FILE}" "${TARGET_FILE}"
chmod +x "${TARGET_FILE}"

if command -v nautilus >/dev/null 2>&1; then
    nautilus -q || true
fi

echo "Installed copy-path to ${TARGET_FILE}"
