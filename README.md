## 🖥️ Build a Basic Web Application using Flask and AWS EC2

### 📌 Project Overview

This project demonstrates how to build and deploy a **simple web application** using **Python Flask** and host it on an **Amazon EC2 instance** (Free Tier). The app takes user input through a form and displays it on a result page.

---

### 🧰 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python Flask
- **Hosting**: AWS EC2 (Amazon Linux 2)
- **Tools**: SSH, pip, yum

---

### ✨ Features

- User input handling via POST
- Displays form data on a separate result page
- Deployed live using EC2 public IP

---

### 📂 Project Structure

```
AWS-Flask-App/
├── app.py
└── templates/
    ├── form.html
    └── result.html
```

---

### 🚀 How to Run (Step-by-Step)

#### 1️⃣ Launch EC2 Instance (AWS Free Tier)
- Go to AWS Console → EC2 → Launch Instance
- Choose Amazon Linux 2 AMI
- Select **t2.micro**
- Add inbound rules for:
  - HTTP (port 80)
  - SSH (port 22)
- Download `.pem` key for SSH

#### 2️⃣ Connect to EC2

```bash
chmod 400 your-key.pem
ssh -i your-key.pem ec2-user@<your-ec2-ip>
```

#### 3️⃣ Install Dependencies

```bash
sudo yum update -y
sudo yum install python3 -y
sudo yum install python3-pip -y
pip3 install flask
```

#### 4️⃣ Upload or Create Files

Create the files manually or upload them using `scp`:

```bash
scp -i your-key.pem -r AWS-Flask-App ec2-user@<your-ec2-ip>:~
```

#### 5️⃣ Run Flask App

Edit `app.py` to include:

```python
app.run(host='0.0.0.0', port=80)
```

Then run:

```bash
sudo python3 app.py
```

#### 6️⃣ Access Your App

Go to:  
```bash
http://<your-ec2-public-ip>
```

---

### 💡 Sample Form Fields

- Name
- Email
- Message
- Favorite Language (dropdown)

---
