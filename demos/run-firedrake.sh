#! /bin/bash

# Inteded for 'rootless podman'. 'root' in the container
# is just the surrounding user. This is needed in order
# to write to the outer file system.

podman run \
  -it --rm \
  -p 127.0.0.1:8899:8888 \
  -w /root \
  -v "$(pwd):/root/demos" \
  docker.io/firedrakeproject/firedrake \
  "/root/demos/run-firedrake-inner.sh"
