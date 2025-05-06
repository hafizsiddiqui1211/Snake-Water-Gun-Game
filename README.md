# 🐍 Snake-Water-Gun Game (Python)

This is a simple command-line implementation of the classic **Snake-Water-Gun** game in Python. It's a variation of Rock-Paper-Scissors with the following rules:

* **Snake drinks Water**
* **Water douses Gun**
* **Gun kills Snake**

---

## 🎮 How to Play

1. Run the script.
2. When prompted, enter your choice:

   * `s` for **Snake**
   * `w` for **Water**
   * `g` for **Gun**
3. The computer randomly selects its choice.
4. The winner is decided based on the rules.

---

## 🧠 Game Logic

| Player | Computer | Result   |
| ------ | -------- | -------- |
| Snake  | Water    | You Win  |
| Snake  | Gun      | You Lose |
| Water  | Gun      | You Win  |
| Water  | Snake    | You Lose |
| Gun    | Snake    | You Win  |
| Gun    | Water    | You Lose |
| Same   | Same     | Tie      |

---

## ✅ Features

* Random choice by the computer using Python's `random` module
* User input validation
* Clear win/loss/tie messages

---

## 🚀 Run the Game

Make sure you have Python installed, then run:

```bash
python snake_water_gun.py
```

---

## 📂 File Structure

```
snake_water_gun.py  # Main game file
README.md           # Project documentation
```

---

## 📜 License

This project is open source and free to use.
