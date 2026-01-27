# Kotlin Rock-Paper-Scissors Game

An Android-based number guessing game developed with Kotlin, showcasing native Android development skills.

## 🎮 Game Introduction
Rock-Paper-Scissors is a traditional finger guessing game where players and computer take turns guessing the total number of fingers shown.

## ✨ Features
- **Intuitive UI**: Clear RadioButton selections and status indicators
- **Smart Turn Mechanism**: Players and computer take turns calling numbers, scorer continues
- **Real-time Score Tracking**: Live score display
- **Complete Game Logic**: Automatic total calculation and result determination
- **One-click Restart**: Reset game state anytime

## 🎯 Game Rules
1. Players can choose to show 0, 5, or 10 fingers
2. When it is the player's turn to call, they can call 0, 5, 10, 15, or 20
3. When it is the computer's turn, the computer randomly calls a number
4. Each round compares the total number of fingers with the called number
5. The caller scores if correct and continues; otherwise, the turn switches
6. Game continues until restart

## 📱 Interface Design
- **Game Status Area**: Displays whose turn it is to call
- **Player Control Area**: Select number of fingers and called number
- **Result Display Area**: Shows detailed results of each round
- **Score Tracking Area**: Displays cumulative score

## 🚀 Quick Start

### Prerequisites
- Android Studio Flamingo or later
- Android SDK 34 or higher
- Kotlin 1.8.0 or higher

### Installation Steps

1. Clone the repository:
\`\`\`bash
git clone <your-project-url>
\`\`\`

2. Open the project in Android Studio:
   - Select "Open an existing project"
   - Navigate to the \`rock-paper-scissors\` folder

3. Wait for Gradle sync to complete

### How to Run

1. Connect an Android device or start an emulator
2. Click the Run button (▶️) in Android Studio
3. Wait for the app to install and launch

## 📁 Project Structure

\`\`\`
rock-paper-scissors/
├── app/
│   ├── src/main/kotlin/com/example/pss_1027/
│   │   └── MainActivity.kt           # Main game logic
│   └── src/main/res/layout/
│       └── activity_main.xml         # User interface layout
├── build.gradle.kts                  # Gradle build configuration
├── README.md                         # Chinese documentation
├── README.en.md                      # English documentation
├── PROJECT_GUIDE.md                  # Project setup guide
└── CHANGELOG.md                      # Version changelog
\`\`\`

## 🛠️ Technologies Used
- **Kotlin**: Primary development language
- **Android SDK**: Native Android development framework
- **Material Design**: Modern UI design
- **ConstraintLayout**: Responsive layout design
- **RadioGroup/RadioButton**: User input controls

## 📝 Code Features
1. **Clean Architecture**: Separation of game logic and UI updates
2. **State-driven Design**: Boolean values manage game turns
3. **Error Prevention**: Handles user input edge cases
4. **Kotlin Idioms**: Effective use of when expressions, extension functions

## 🔄 Future Enhancements
1. **Add Animations**: Finger movement animations, scoring effects
2. **Sound System**: Button sounds, scoring sounds, background music
3. **Enhanced AI**: Adjust computer strategy based on history
4. **Multi-language Support**: Chinese/English interface switching
5. **Game History**: Save past scores and game statistics
6. **Online Multiplayer**: Two-player battles via Bluetooth or internet

## 📸 Screenshots
(Screenshots to be added)

## ⚠️ Notes
- Requires Android 8.0 (API 26) or higher
- Recommended to run on physical device or high-performance emulator
- First run requires Gradle dependency downloads

## 📝 License
MIT License

---

## 🌐 Language Versions
- [中文版本](README.md)
- [English Version](README.en.md)
