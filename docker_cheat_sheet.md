
# Docker Cheat Sheet

## 1. Installation

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
sudo docker run hello-world

# Add user to docker group (to run without sudo)
sudo usermod -aG docker $USER
newgrp docker
```

### Linux (CentOS/RHEL/Fedora)
```bash
# Remove old versions
sudo yum remove docker docker-client docker-client-latest docker-common docker-latest

# Install using repository
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
sudo docker run hello-world
```

### macOS
```bash
# Using Homebrew
brew install --cask docker

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Verify installation
docker --version
docker run hello-world
```

### Windows
```powershell
# Install using Chocolatey
choco install docker-desktop

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Verify installation (in PowerShell)
docker --version
docker run hello-world
```

## 2. Basic Docker Commands

| Command | Description |
| ------- | ----------- |
| `docker --version` | Display Docker version |
| `docker info` | Display system-wide information about Docker |
| `docker help` | Get help on Docker commands |
| `docker login` | Log in to a Docker registry |
| `docker logout` | Log out from a Docker registry |

## 3. Container Management

### Running Containers
| Command | Description |
| ------- | ----------- |
| `docker run <image>` | Run a container from an image |
| `docker run -d <image>` | Run container in detached mode (background) |
| `docker run -it <image>` | Run container in interactive mode with terminal |
| `docker run --name <name> <image>` | Run container with a specific name |
| `docker run -p <host_port>:<container_port> <image>` | Map ports (host:container) |
| `docker run -v <host_path>:<container_path> <image>` | Mount volume (host:container) |
| `docker run -e <key>=<value> <image>` | Set environment variable |
| `docker run --rm <image>` | Automatically remove container when it exits |
| `docker run --restart=always <image>` | Always restart container if it stops |

### Container Lifecycle
| Command | Description |
| ------- | ----------- |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker start <container>` | Start a stopped container |
| `docker stop <container>` | Stop a running container |
| `docker restart <container>` | Restart a container |
| `docker pause <container>` | Pause a running container |
| `docker unpause <container>` | Unpause a paused container |
| `docker kill <container>` | Force stop a container |
| `docker rm <container>` | Remove a stopped container |
| `docker rm -f <container>` | Force remove a running container |

### Inspecting Containers
| Command | Description |
| ------- | ----------- |
| `docker logs <container>` | View container logs |
| `docker logs -f <container>` | Follow container logs in real-time |
| `docker logs --tail <n> <container>` | View last n lines of logs |
| `docker inspect <container>` | View detailed container information |
| `docker top <container>` | Display running processes in a container |
| `docker stats` | Display live resource usage statistics |
| `docker stats <container>` | Display stats for specific container |
| `docker port <container>` | List port mappings for a container |

### Executing Commands in Containers
| Command | Description |
| ------- | ----------- |
| `docker exec <container> <command>` | Execute a command in a running container |
| `docker exec -it <container> bash` | Open interactive bash shell in container |
| `docker exec -it <container> sh` | Open interactive sh shell in container |
| `docker attach <container>` | Attach to a running container |
| `docker cp <container>:<path> <host_path>` | Copy files from container to host |
| `docker cp <host_path> <container>:<path>` | Copy files from host to container |

## 4. Image Management

### Working with Images
| Command | Description |
| ------- | ----------- |
| `docker images` | List all images |
| `docker images -a` | List all images (including intermediate) |
| `docker pull <image>` | Pull an image from a registry |
| `docker pull <image>:<tag>` | Pull a specific version/tag of an image |
| `docker push <image>` | Push an image to a registry |
| `docker rmi <image>` | Remove an image |
| `docker rmi -f <image>` | Force remove an image |
| `docker tag <image> <new_image>:<tag>` | Tag an image |
| `docker history <image>` | Show image history/layers |
| `docker inspect <image>` | View detailed image information |

### Building Images
| Command | Description |
| ------- | ----------- |
| `docker build -t <name>:<tag> .` | Build image from Dockerfile in current directory |
| `docker build -t <name>:<tag> -f <dockerfile> .` | Build using specific Dockerfile |
| `docker build --no-cache -t <name>:<tag> .` | Build without using cache |
| `docker build --build-arg <key>=<value> -t <name>:<tag> .` | Build with build arguments |
| `docker commit <container> <image>:<tag>` | Create image from container |
| `docker save <image> > <file>.tar` | Save image to tar archive |
| `docker load < <file>.tar` | Load image from tar archive |
| `docker export <container> > <file>.tar` | Export container filesystem as tar |
| `docker import <file>.tar <image>:<tag>` | Import container from tar file |

### Searching Images
| Command | Description |
| ------- | ----------- |
| `docker search <term>` | Search for images on Docker Hub |
| `docker search --filter stars=<n> <term>` | Search images with at least n stars |
| `docker search --filter is-official=true <term>` | Search only official images |

## 5. Docker Networking

### Network Commands
| Command | Description |
| ------- | ----------- |
| `docker network ls` | List all networks |
| `docker network create <network>` | Create a network |
| `docker network create --driver bridge <network>` | Create a bridge network |
| `docker network rm <network>` | Remove a network |
| `docker network inspect <network>` | View network details |
| `docker network connect <network> <container>` | Connect container to network |
| `docker network disconnect <network> <container>` | Disconnect container from network |
| `docker network prune` | Remove unused networks |

### Network Drivers
```bash
# Bridge network (default) - for standalone containers
docker network create --driver bridge my-bridge-network

# Host network - container shares host's network
docker run --network host <image>

# None network - no network access
docker run --network none <image>

# Overlay network - for Swarm services
docker network create --driver overlay my-overlay-network

# Macvlan network - assign MAC address to container
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 my-macvlan
```

## 6. Docker Volumes and Storage

### Volume Commands
| Command | Description |
| ------- | ----------- |
| `docker volume ls` | List all volumes |
| `docker volume create <volume>` | Create a volume |
| `docker volume inspect <volume>` | View volume details |
| `docker volume rm <volume>` | Remove a volume |
| `docker volume prune` | Remove unused volumes |

### Using Volumes
```bash
# Named volume
docker run -v my-volume:/data <image>

# Bind mount (absolute path)
docker run -v /host/path:/container/path <image>

# Bind mount (relative path)
docker run -v $(pwd):/container/path <image>

# Read-only volume
docker run -v my-volume:/data:ro <image>

# Anonymous volume
docker run -v /data <image>

# Volume from another container
docker run --volumes-from <container> <image>
```

### tmpfs Mounts (Linux only)
```bash
# Mount tmpfs (temporary filesystem in memory)
docker run --tmpfs /app:rw,size=64m,mode=1770 <image>
```

## 7. Docker Compose

### Basic Commands
| Command | Description |
| ------- | ----------- |
| `docker compose up` | Start services defined in docker-compose.yml |
| `docker compose up -d` | Start services in detached mode |
| `docker compose down` | Stop and remove containers, networks |
| `docker compose down -v` | Also remove volumes |
| `docker compose start` | Start existing containers |
| `docker compose stop` | Stop running containers |
| `docker compose restart` | Restart services |
| `docker compose pause` | Pause services |
| `docker compose unpause` | Unpause services |
| `docker compose ps` | List containers |
| `docker compose logs` | View output from containers |
| `docker compose logs -f` | Follow log output |
| `docker compose exec <service> <command>` | Execute command in service container |
| `docker compose build` | Build or rebuild services |
| `docker compose pull` | Pull service images |
| `docker compose push` | Push service images |
| `docker compose config` | Validate and view compose file |

### Sample docker-compose.yml
```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - webnet
    depends_on:
      - db
    environment:
      - ENV=production
    restart: always

  db:
    image: postgres:15
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - webnet
    environment:
      POSTGRES_PASSWORD: example
      POSTGRES_USER: user
      POSTGRES_DB: mydb
    restart: always

networks:
  webnet:
    driver: bridge

volumes:
  db-data:
```

## 8. Dockerfile

### Dockerfile Instructions
| Instruction | Description |
| ----------- | ----------- |
| `FROM <image>` | Set base image |
| `FROM <image>:<tag>` | Set base image with specific version |
| `WORKDIR <path>` | Set working directory |
| `COPY <src> <dest>` | Copy files from host to image |
| `ADD <src> <dest>` | Copy files (also supports URLs and auto-extraction) |
| `RUN <command>` | Execute command during build |
| `CMD ["executable","param1"]` | Default command to run when container starts |
| `ENTRYPOINT ["executable"]` | Configure container as executable |
| `ENV <key>=<value>` | Set environment variable |
| `ARG <name>=<default>` | Define build-time variable |
| `EXPOSE <port>` | Document which ports the container listens on |
| `VOLUME <path>` | Create mount point for volumes |
| `USER <user>` | Set user for RUN, CMD, ENTRYPOINT |
| `LABEL <key>=<value>` | Add metadata to image |
| `HEALTHCHECK` | Define health check command |

### Sample Dockerfile (Node.js App)
```dockerfile
# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001 && \
    chown -R nodejs:nodejs /app

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js

# Start application
CMD ["node", "server.js"]
```

### Sample Dockerfile (Python App)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
```

### Multi-stage Build Example
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### Best Practices for Dockerfiles
```dockerfile
# 1. Use specific image versions
FROM node:18.17.0-alpine3.18

# 2. Use .dockerignore to exclude files
# Create .dockerignore file with:
# node_modules
# npm-debug.log
# .git
# .env

# 3. Minimize layers - combine RUN commands
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    rm -rf /var/lib/apt/lists/*

# 4. Order layers from least to most frequently changing
COPY package*.json ./
RUN npm install
COPY . .

# 5. Use COPY instead of ADD (unless you need ADD features)
COPY . .

# 6. Run as non-root user
USER node

# 7. Use multi-stage builds to reduce image size
```

## 9. Docker Registry Operations

### Docker Hub
| Command | Description |
| ------- | ----------- |
| `docker login` | Log in to Docker Hub |
| `docker logout` | Log out from Docker Hub |
| `docker push <username>/<image>:<tag>` | Push image to Docker Hub |
| `docker pull <username>/<image>:<tag>` | Pull image from Docker Hub |
| `docker search <term>` | Search Docker Hub for images |

### Private Registry
```bash
# Run local registry
docker run -d -p 5000:5000 --restart=always --name registry registry:2

# Tag image for private registry
docker tag my-image localhost:5000/my-image

# Push to private registry
docker push localhost:5000/my-image

# Pull from private registry
docker pull localhost:5000/my-image

# Login to private registry
docker login registry.example.com

# Push to private registry
docker tag my-image registry.example.com/my-image
docker push registry.example.com/my-image
```

## 10. Cleaning Up Docker (Storage Management)

### Remove Unused Resources
| Command | Description |
| ------- | ----------- |
| `docker system df` | Show Docker disk usage |
| `docker system prune` | Remove unused containers, networks, images |
| `docker system prune -a` | Remove all unused images (not just dangling) |
| `docker system prune -a --volumes` | Remove all unused data including volumes |
| `docker system prune --filter "until=24h"` | Remove resources older than 24 hours |

### Remove Specific Resources
| Command | Description |
| ------- | ----------- |
| `docker container prune` | Remove all stopped containers |
| `docker image prune` | Remove dangling images |
| `docker image prune -a` | Remove all unused images |
| `docker volume prune` | Remove unused volumes |
| `docker network prune` | Remove unused networks |
| `docker builder prune` | Remove build cache |

### Aggressive Cleanup
```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)

# Remove all networks (except default ones)
docker network rm $(docker network ls -q)

# Complete cleanup
docker system prune -a --volumes -f
```

### Filtering and Selective Cleanup
```bash
# Remove containers exited more than 24 hours ago
docker container prune --filter "until=24h"

# Remove images created more than 7 days ago
docker image prune -a --filter "until=168h"

# Remove containers with specific label
docker container prune --filter "label=app=myapp"

# Show what would be removed (dry run)
docker system prune --dry-run
```

### Disk Space Management
```bash
# Check Docker disk usage
docker system df

# Detailed disk usage
docker system df -v

# Check size of specific container
docker ps -s

# Check size of all containers
docker ps -a -s

# Find largest images
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" | sort -k 3 -h

# Clean build cache
docker builder prune --all
```

## 11. Common Issues and Troubleshooting

### Permission Issues (Linux)
```bash
# Permission denied error
# Solution: Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Or run with sudo
sudo docker run hello-world
```

### Port Already in Use
```bash
# Error: port is already allocated
# Solution 1: Find and kill process using the port
sudo lsof -i :8080
sudo kill -9 <PID>

# Solution 2: Use different port
docker run -p 8081:80 nginx

# Solution 3: Stop container using the port
docker ps
docker stop <container>
```

### Container Keeps Restarting
```bash
# Check logs to see what's failing
docker logs <container>
docker logs --tail 100 <container>

# Check events
docker events --filter container=<container>

# Run without restart policy to debug
docker run --rm <image>

# Override entrypoint to investigate
docker run -it --entrypoint /bin/sh <image>
```

### Out of Disk Space
```bash
# Check disk usage
docker system df

# Clean up aggressively
docker system prune -a --volumes

# Check for large log files
sudo du -sh /var/lib/docker/containers/*/*-json.log

# Limit container log size in daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}

# Restart Docker daemon
sudo systemctl restart docker
```

### DNS Resolution Issues
```bash
# Container can't resolve DNS
# Solution 1: Specify DNS servers
docker run --dns 8.8.8.8 --dns 8.8.4.4 <image>

# Solution 2: Update daemon.json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}

# Solution 3: Check network settings
docker network inspect bridge
```

### Cannot Connect to Docker Daemon
```bash
# Error: Cannot connect to the Docker daemon
# Solution 1: Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Solution 2: Check if Docker is running
sudo systemctl status docker

# Solution 3: Check socket permissions
sudo chmod 666 /var/run/docker.sock

# Solution 4: Restart Docker
sudo systemctl restart docker
```

### Image Pull Failures
```bash
# Error: pull access denied or image not found
# Solution 1: Check image name and tag
docker pull nginx:latest

# Solution 2: Login if pulling from private registry
docker login

# Solution 3: Try with explicit registry
docker pull docker.io/library/nginx:latest

# Solution 4: Check network connectivity
ping registry-1.docker.io
```

### Container Networking Issues
```bash
# Can't access container from host
# Check port mapping
docker port <container>

# Check if container is running
docker ps

# Check container IP
docker inspect <container> | grep IPAddress

# Test connectivity from host
curl http://localhost:8080

# Test from inside container
docker exec <container> curl http://localhost:80
```

### Build Cache Issues
```bash
# Build not picking up changes
# Solution: Build without cache
docker build --no-cache -t <image> .

# Or remove specific layers
docker builder prune

# Check build cache
docker system df -v | grep BuildCache
```

### Container Exited Immediately
```bash
# Container starts and stops immediately
# Check logs
docker logs <container>

# Run interactively to debug
docker run -it <image> /bin/sh

# Check if CMD/ENTRYPOINT is correct
docker inspect <image> | grep -A 10 Config

# Override entrypoint for debugging
docker run -it --entrypoint /bin/bash <image>
```

## 12. Configuration and Optimization

### Docker Daemon Configuration
```bash
# Edit daemon configuration
sudo nano /etc/docker/daemon.json
```

### Sample daemon.json
```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3",
    "compress": "true"
  },
  "storage-driver": "overlay2",
  "dns": ["8.8.8.8", "8.8.4.4"],
  "default-address-pools": [
    {
      "base": "172.17.0.0/12",
      "size": 24
    }
  ],
  "max-concurrent-downloads": 10,
  "max-concurrent-uploads": 10,
  "builder": {
    "gc": {
      "enabled": true,
      "defaultKeepStorage": "20GB"
    }
  },
  "features": {
    "buildkit": true
  }
}
```

### Resource Limits
```bash
# Limit memory
docker run -m 512m <image>

# Limit memory with swap
docker run -m 512m --memory-swap 1g <image>

# Limit CPU
docker run --cpus=1.5 <image>

# CPU shares (relative weight)
docker run --cpu-shares=512 <image>

# Set CPU affinity
docker run --cpuset-cpus="0,1" <image>

# Limit I/O
docker run --device-read-bps /dev/sda:1mb <image>
docker run --device-write-bps /dev/sda:1mb <image>
```

### Performance Optimization
```bash
# Use BuildKit for faster builds
export DOCKER_BUILDKIT=1
docker build -t <image> .

# Parallel builds
docker build --build-arg BUILDKIT_INLINE_CACHE=1 -t <image> .

# Use build cache from registry
docker build --cache-from <image> -t <image> .

# Multi-stage builds for smaller images
# See Multi-stage Build Example above

# Use .dockerignore to speed up builds
# Exclude unnecessary files from build context

# Use alpine images for smaller size
FROM node:18-alpine
```

## 13. Security Best Practices

### Image Security
```bash
# Scan images for vulnerabilities (newer method)
docker scout cves <image>

# Older method (deprecated)
# docker scan <image>

# Use official images
docker pull nginx:latest

# Use specific versions (not latest)
docker pull nginx:1.24.0

# Run as non-root user
USER node

# Read-only filesystem
docker run --read-only <image>

# Drop capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE <image>

# Use security options
docker run --security-opt=no-new-privileges:true <image>
```

### Container Security
```bash
# Limit container resources
docker run --memory="256m" --cpus="1" <image>

# Use user namespace
docker run --userns=host <image>

# Set SELinux labels
docker run --security-opt label=level:s0:c100,c200 <image>

# AppArmor profile
docker run --security-opt apparmor=docker-default <image>

# Seccomp profile
docker run --security-opt seccomp=default.json <image>

# Prevent privilege escalation
docker run --security-opt=no-new-privileges:true <image>
```

### Best Practices
```bash
# 1. Keep Docker updated
sudo apt-get update && sudo apt-get upgrade docker-ce

# 2. Use trusted registries
# Configure in daemon.json
{
  "insecure-registries": [],
  "registry-mirrors": []
}

# 3. Sign images
docker trust sign <image>:<tag>

# 4. Scan for secrets
# Use tools like git-secrets or truffleHog

# 5. Minimize attack surface
# Use minimal base images
FROM alpine:3.18

# 6. Keep secrets out of images
# Use environment variables or secrets management
docker run -e DB_PASSWORD=secret <image>
docker secret create my_secret secret.txt

# 7. Regular security audits
docker inspect <container>
docker history <image>
```

## 14. Multi-Platform Builds

### BuildX for Multi-Architecture
```bash
# Create and use builder
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap

# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t <image> .

# Build and push
docker buildx build --platform linux/amd64,linux/arm64 -t <username>/<image>:latest --push .

# List available builders
docker buildx ls

# Inspect current builder
docker buildx inspect

# Remove builder
docker buildx rm mybuilder
```

### Platform-Specific Instructions
```dockerfile
# Use platform-specific base image
FROM --platform=$BUILDPLATFORM golang:1.21-alpine AS builder

# Set target architecture
ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "Building on $BUILDPLATFORM for $TARGETPLATFORM"

# Build for specific architecture
ARG TARGETARCH
RUN CGO_ENABLED=0 GOARCH=$TARGETARCH go build -o app
```

## 15. Docker Context

### Managing Docker Contexts
| Command | Description |
| ------- | ----------- |
| `docker context ls` | List available contexts |
| `docker context create <name>` | Create new context |
| `docker context use <name>` | Switch to context |
| `docker context inspect <name>` | View context details |
| `docker context rm <name>` | Remove context |

### Remote Docker Host
```bash
# Create context for remote host
docker context create remote --docker "host=ssh://user@remote-host"

# Use remote context
docker context use remote

# Run commands on remote host
docker ps

# Switch back to default
docker context use default
```

## 16. Performance Tips

### Speed Up Builds
```bash
# 1. Use BuildKit
export DOCKER_BUILDKIT=1

# 2. Optimize layer caching
# Copy dependency files first
COPY package*.json ./
RUN npm install
COPY . .

# 3. Use .dockerignore
# Exclude unnecessary files

# 4. Use multi-stage builds
# Separate build and runtime stages

# 5. Parallel stages
# BuildKit can parallelize independent stages

# 6. Mount cache for package managers
RUN --mount=type=cache,target=/root/.npm npm install
```

### Reduce Image Size
```bash
# 1. Use alpine base images
FROM node:18-alpine

# 2. Multi-stage builds
# Copy only necessary artifacts from build stage

# 3. Minimize layers
# Combine RUN commands with &&

# 4. Remove unnecessary files
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*

# 5. Use .dockerignore
# Exclude development files

# 6. Compress image layers
docker save <image> | gzip > image.tar.gz
```

### Optimize Runtime Performance
```bash
# 1. Allocate appropriate resources
docker run -m 2g --cpus=2 <image>

# 2. Use volumes for I/O intensive operations
docker run -v /data:/data <image>

# 3. Use host network for best performance (less secure)
docker run --network host <image>

# 4. Tune storage driver
# Use overlay2 (default on most systems)

# 5. Enable BuildKit features
{
  "features": {
    "buildkit": true
  }
}

# 6. Use tmpfs for temporary data
docker run --tmpfs /tmp:rw,size=100m <image>
```

## 17. Monitoring and Logging

### Container Monitoring
```bash
# Real-time stats
docker stats

# Stats for specific container
docker stats <container>

# Stats in JSON format
docker stats --no-stream --format "{{json .}}"

# Resource usage
docker ps -a -s

# Inspect resource limits
docker inspect <container> | grep -A 10 HostConfig
```

### Logging
```bash
# View logs
docker logs <container>

# Follow logs
docker logs -f <container>

# Last n lines
docker logs --tail 100 <container>

# Logs since timestamp
docker logs --since 2024-01-01T00:00:00 <container>

# Logs with timestamps
docker logs -t <container>

# Configure log driver
docker run --log-driver json-file \
           --log-opt max-size=10m \
           --log-opt max-file=3 \
           <image>
```

### Log Drivers
```bash
# Available log drivers:
# - json-file (default)
# - syslog
# - journald
# - gelf
# - fluentd
# - awslogs
# - splunk
# - gcplogs

# Use syslog driver
docker run --log-driver syslog <image>

# Configure in daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

## 18. Health Checks

### Dockerfile Health Check
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

### Docker Compose Health Check
```yaml
services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 40s
```

### Check Container Health
```bash
# View health status
docker ps

# Inspect health check
docker inspect --format='{{json .State.Health}}' <container>

# View health check logs
docker inspect <container> | jq '.[0].State.Health'
```

## 19. Docker Swarm (Orchestration)

### Basic Swarm Commands
| Command | Description |
| ------- | ----------- |
| `docker swarm init` | Initialize swarm mode |
| `docker swarm join` | Join swarm as worker |
| `docker swarm leave` | Leave swarm |
| `docker node ls` | List swarm nodes |
| `docker service create` | Create service |
| `docker service ls` | List services |
| `docker service ps <service>` | List service tasks |
| `docker service scale <service>=<n>` | Scale service |
| `docker service rm <service>` | Remove service |

### Example Swarm Service
```bash
# Initialize swarm
docker swarm init

# Create service
docker service create --name web --replicas 3 -p 80:80 nginx

# Scale service
docker service scale web=5

# Update service
docker service update --image nginx:1.24 web

# Remove service
docker service rm web
```

## 20. Tips and Tricks

### Useful Aliases
```bash
# Add to ~/.bashrc or ~/.zshrc
alias dps='docker ps'
alias dpsa='docker ps -a'
alias di='docker images'
alias drm='docker rm'
alias drmi='docker rmi'
alias dex='docker exec -it'
alias dlogs='docker logs -f'
alias dstop='docker stop $(docker ps -q)'
alias dclean='docker system prune -a --volumes -f'
```

### One-Liners
```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -q)

# Get container IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>

# Execute command in all running containers
docker ps -q | xargs -I {} docker exec {} <command>

# Copy file to all running containers
for c in $(docker ps -q); do docker cp file.txt $c:/path/; done

# Show container size
docker ps -s --format "table {{.Names}}\t{{.Size}}"
```

### Debugging
```bash
# Run container and delete when exit
docker run --rm -it <image> /bin/sh

# Override entrypoint for debugging
docker run -it --entrypoint /bin/bash <image>

# Inspect running container
docker exec -it <container> /bin/sh

# Check environment variables
docker exec <container> env

# Check process list
docker top <container>

# Stream events
docker events

# Check Docker info
docker info

# Verify Dockerfile syntax
docker build -t test . --no-cache --progress=plain
```

### Best Practices Summary
1. **Use specific image tags** - Avoid `latest` in production
2. **Multi-stage builds** - Keep final images small
3. **Use .dockerignore** - Exclude unnecessary files
4. **Run as non-root** - Security best practice
5. **One process per container** - Follow Unix philosophy
6. **Use volumes for data** - Keep containers stateless
7. **Health checks** - Monitor container health
8. **Resource limits** - Prevent resource exhaustion
9. **Logging strategy** - Configure log rotation
10. **Regular cleanup** - Manage disk space
11. **Layer optimization** - Minimize and order layers wisely
12. **Security scanning** - Scan images for vulnerabilities
13. **Documentation** - Comment Dockerfiles and compose files
14. **Version control** - Track Dockerfile changes
15. **Testing** - Test images before deploying

---

**Last Updated**: January 2024

**Maintained by**: Community Contributors

For more information, visit [Docker Documentation](https://docs.docker.com/)
