# 🌐 Docker Networking 



# 🧰 Prerequisites

Make sure Docker is installed:

```bash
docker --version
```

---

# 🚀 Step-by-Step Demo

---

## 🔹 Step 1: Create a Network

```bash
docker network create mynet
```

👉 Creates a custom Docker network named `mynet`

---

## 🔹 Step 2: Run First Container

```bash
docker run -dit --name c1 --network mynet alpine sh
```

👉 Starts container `c1` inside `mynet`

---

## 🔹 Step 3: Run Second Container

```bash
docker run -dit --name c2 --network mynet alpine sh
```

👉 Starts container `c2` inside same network

---

## 🔹 Step 4: Access Container c1

```bash
docker exec -it c1 sh
```

---

## 🔹 Step 5: Install Ping Tool

```bash
apk add iputils
```

👉 Needed to test connectivity

---

## 🔹 Step 6: Ping Container c2

```bash
ping c2
```

👉 ✅ Expected Output:

```text
PING c2 (172.x.x.x): 56 data bytes
```

---

# 🎉 Result

✔ Containers communicate using **names (c2)**
✔ No need to use IP addresses

---

# 🔍 Inspect Network

```bash
docker network inspect mynet
```

👉 Shows:

* Connected containers
* IP addresses
* Network details

---

# ❌ Failure Case (Important)

---

## 🔹 Step 7: Run Container Outside Network

```bash
docker run -dit --name c3 alpine sh
```

---

## 🔹 Step 8: Try to Ping c1

```bash
docker exec -it c3 sh
apk add iputils
ping c1
```

👉 ❌ This will FAIL

---

# 💡 Why Did It Fail?

👉 `c3` is not part of `mynet`
👉 Containers must be in same network to communicate

---

# 🧠 Key Learnings

| Scenario          | Result                |
| ----------------- | --------------------- |
| Same network      | Communication works ✅ |
| Different network | Communication fails ❌ |

---

# 🔥 Real-World Example

```text
Frontend → Backend → Database
```

👉 All must be connected to the same network

---

# 🧠 One-line Summary

👉 Containers can communicate only when they are in the same Docker network

---

# 🧹 Cleanup (Optional)

```bash
docker rm -f c1 c2 c3
docker network rm mynet
```
