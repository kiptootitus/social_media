#!/bin/bash

# Exit immediately on error
set -e

echo "🧹 Removing Snap-installed Node and Yarn (if any)..."
sudo snap remove node --purge || echo "Node snap not installed"
sudo snap remove yarn --purge || echo "Yarn snap not installed"

echo "📥 Installing NVM..."
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Load nvm immediately for the rest of the script
export NVM_DIR="$HOME/.nvm"
# shellcheck disable=SC1090
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

echo "📦 Installing latest LTS version of Node.js via NVM..."
nvm install --lts

echo "🧰 Enabling Corepack (Yarn/Bun package manager support)..."
corepack enable
corepack prepare yarn@stable --activate

echo "✅ Done. Run 'yarn --version' and 'node --version' to verify."
