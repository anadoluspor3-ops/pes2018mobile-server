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
