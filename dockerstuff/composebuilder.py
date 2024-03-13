import argparse

def generate_docker_compose(num_workers):
    docker_compose_content = f"""version: "2.4"
services:"""

    for i in range(1, num_workers + 1):
        docker_compose_content += f"""
  worker{i}:
    image: project:v0
    command: /bin/bash -c "hadoop-3.3.6/bin/hdfs --daemon start datanode && usr/local/spark/sbin/start-worker.sh spark://192.168.2.62:7077"
    expose:
      - "50010"
      - "9866"
      - "9867"
      - "7077"
      - "9000"
      - "9001"
    volumes:
      - /home/ubuntu/Drive:/Drive
    mem_limit: 1600M
"""

    with open('docker-compose.yml', 'w') as f:
        f.write(docker_compose_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Docker Compose file for Spark cluster")
    parser.add_argument("num_workers", type=int, help="Number of Spark workers")
    args = parser.parse_args()

    generate_docker_compose(args.num_workers)
