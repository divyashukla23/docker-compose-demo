# 🐳 Docker Swarm Demo (Step-by-Step Commands)

---

# 🚀 Step-by-Step Commands for Swarm demo:

---

## 🔹 Step 1: Initialize Swarm

```bash
docker swarm init
```

---

## 🔹 Step 2: Check Nodes

```bash
docker node ls
```

---

## 🔹 Step 3: Create a Service

```bash
docker service create --name myapp -p 8080:80 nginx
```

---

## 🔹 Step 4: List Services

```bash
docker service ls
```

---

## 🔹 Step 5: Check Service Tasks (Containers)

```bash
docker service ps myapp
```

---

## 🔹 Step 6: Access Application

Open in browser:

```text
http://localhost:8080
```

---

# 🔥 Scaling Demo

---

## 🔹 Step 7: Scale Service

```bash
docker service scale myapp=3
```

---

## 🔹 Step 8: Verify Scaling

```bash
docker service ps myapp
```

---

# 💥 Self-Healing Demo

---

## 🔹 Step 9: List Running Containers

```bash
docker ps
```

---

## 🔹 Step 10: Kill a Container

```bash
docker kill <container_id>
```

---

## 🔹 Step 11: Check Service Again

```bash
docker service ps myapp
```

👉 Swarm will recreate the container automatically

---

# 🔄 Update Service

---

## 🔹 Step 12: Update Image

```bash
docker service update --image nginx:alpine myapp
```

---

# 🛑 Cleanup

---

## 🔹 Step 13: Remove Service

```bash
docker service rm myapp
```

---

## 🔹 Step 14: Leave Swarm

```bash
docker swarm leave --force
```

---

#  Key Commands Summary

| Action         | Command                 |
| -------------- | ----------------------- |
| Init swarm     | `docker swarm init`     |
| List nodes     | `docker node ls`        |
| Create service | `docker service create` |
| List services  | `docker service ls`     |
| Scale service  | `docker service scale`  |
| Check tasks    | `docker service ps`     |
| Update service | `docker service update` |
| Remove service | `docker service rm`     |
| Leave swarm    | `docker swarm leave`    |

---

#  Summary

Docker Swarm allows you to deploy, scale, and manage containers across a cluster using simple commands

