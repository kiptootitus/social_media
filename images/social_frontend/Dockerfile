# Stage 1: Build the application
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency files
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build

# Stage 2: Serve the app with a lightweight server
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install a static file server
RUN npm install -g serve

# Copy built files from the builder stage
COPY --from=builder /app/build ./build

# Expose the port the app will run on
EXPOSE 3000

# Command to run the server
CMD ["serve", "-s", "build", "-l", "3000"]
