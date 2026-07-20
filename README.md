# PES 2018 Mobile - Custom Server Emulator 

This project is a Flask-based custom server emulator designed to mimic and handle network requests (API) for **PES 2018 Mobile** (eFootball).

All data traffic between the game client and the server is encrypted, compressed, and packed for security. This server decrypts these complex payloads, processes them, and returns the appropriate game responses (such as EULA setups, user creation, MyClub menus, and more).

---

## 🚀 Features

* **Secure Traffic Management:** Incoming requests are automatically decrypted using `Blowfish (CBC Mode)`, decompressed with `zlib`, and unpacked via `msgpack` before processing.
* **Dynamic Response Syncing:** Dynamically synchronizes the game client's `rqid` (request ID) within responses to prevent handshake errors or disconnects.
* **Extensive API Coverage:** Implements crucial game endpoints, including:
* Server environment config (`CmdGetServerEnv`)
* User creation and authentication (`CmdCreateUser`, `CmdLogin`)
* MyClub main menus, achievements, and manager contract norms
* Country configurations and product listings


* **Deployment Ready:** Supports dynamic cloud port allocation (`os.environ.get("PORT")`), making it immediately compatible with platforms like Render or Heroku right out of the box.

---

## 🛠️ Project Structure

For the server to function properly, ensure your repository layout matches the structure below:

```text
pes2018mobile-server/
│
├── server.py              # Main Flask application entry point
├── decorators.py          # Custom decorators including @encrypt_response
├── myclub.py              # Helper module to construct MyClub payloads
└── responses/             # JSON folder storing structural static responses
    ├── GetCountryList.json
    ├── set_myclub_entry_info.json
    ├── CmdLogin.json
    └── ...

```

---

## 📦 Installation & Setup

### 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install Flask pycryptodome msgpack

```

### 2. Run the Server

Launch the main server file to start your local emulation environment:

```bash
python server.py

```

The server will spin up over plain **HTTP** at `[http://0.0.0.0:8080](http://0.0.0.0:8080)` by default (or bind itself to your environment's designated `PORT`).

---

## 🔒 Crypto Specifications

The endpoint wrapper uses a static 112-character hex key converted into binary bytes. Every incoming payload expects an initial 8-byte segment reserved exclusively for the `IV` (Initialization Vector), followed immediately by the encrypted ciphertext.

---

💡 *Feel free to open an issue or submit a pull request if you want to contribute to expanding the supported endpoint structure!*

##  Screenshots
<img width="1280" height="692" alt="5922409256218988622 (1)" src="https://github.com/user-attachments/assets/d10fd255-21a1-4740-baa6-fdc16cfd656f" />

<img width="1280" height="690" alt="5922409256218988720 (1)" src="https://github.com/user-attachments/assets/2f3bf4a5-6a7e-4852-88e0-6cab897d1e47" />

<img width="1280" height="692" alt="5922409256218988723 (3)" src="https://github.com/user-attachments/assets/5de335ce-3436-4444-9fbd-85d33f16d4ab" />

<img width="1280" height="768" alt="5960579781629775584" src="https://github.com/user-attachments/assets/81e61792-2be8-48ef-ac70-35ef62fd73d9" />

<img width="1280" height="768" alt="5960579781629775588" src="https://github.com/user-attachments/assets/3f7dab54-8d28-45c9-b2a1-d751ce5e98c8" />



