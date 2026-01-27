package com.example.pss_1027

import android.os.Bundle
import android.widget.Button
import android.widget.RadioGroup
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    // 遊戲狀態
    private var isPlayerTurn = true  // true=玩家喊聲，false=電腦喊聲
    private var playerScore = 0
    private var computerScore = 0

    // 可出的數字（手指）
    private val fingerNumbers = arrayOf(0, 5, 10)
    // 可喊的數字
    private val callNumbers = arrayOf(0, 5, 10, 15, 20)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // 取得所有元件
        val tvTurn = findViewById<TextView>(R.id.tvTurn)
        val tvCaller = findViewById<TextView>(R.id.tvCaller)
        val radioGroupNumber = findViewById<RadioGroup>(R.id.radioGroupNumber)
        val radioGroupCall = findViewById<RadioGroup>(R.id.radioGroupCall)
        val btnAction = findViewById<Button>(R.id.btnAction)
        val btnRestart = findViewById<Button>(R.id.btnRestart)

        // 結果顯示元件
        val tvPlayerResult = findViewById<TextView>(R.id.tvPlayerResult)
        val tvComputerResult = findViewById<TextView>(R.id.tvComputerResult)
        val tvCallResult = findViewById<TextView>(R.id.tvCallResult)
        val tvTotalResult = findViewById<TextView>(R.id.tvTotalResult)
        val tvFinalResult = findViewById<TextView>(R.id.tvFinalResult)
        val tvScore = findViewById<TextView>(R.id.tvScore)

        // 初始化遊戲
        initGame()
        updateUI(tvTurn, tvCaller, radioGroupCall, btnAction)

        btnAction.setOnClickListener {
            if (isPlayerTurn) {
                // 玩家喊聲的回合
                playPlayerTurn(
                    radioGroupNumber,
                    radioGroupCall,
                    tvPlayerResult,
                    tvComputerResult,
                    tvCallResult,
                    tvTotalResult,
                    tvScore,
                    tvTurn,
                    tvCaller
                )
            } else {
                // 電腦喊聲的回合
                playComputerTurn(
                    radioGroupNumber,
                    tvPlayerResult,
                    tvComputerResult,
                    tvCallResult,
                    tvTotalResult,
                    tvScore,
                    tvTurn,
                    tvCaller
                )
            }

            // 更新按鈕文字
            btnAction.text = if (isPlayerTurn) "玩家喊聲" else "電腦喊聲"

            // 解鎖/鎖定喊聲選擇
            updateUI(tvTurn, tvCaller, radioGroupCall, btnAction)
        }

        btnRestart.setOnClickListener {
            initGame()
            updateUI(tvTurn, tvCaller, radioGroupCall, btnAction)

            // 清空結果
            tvPlayerResult.text = "玩家出拳："
            tvComputerResult.text = "電腦出拳："
            tvCallResult.text = "本回合喊："
            tvTotalResult.text = "總和："
            tvScore.text = "比分：玩家 $playerScore - $computerScore 電腦"

            // 重置選擇
            radioGroupNumber.check(R.id.btnNumber0)
            radioGroupCall.check(R.id.btnCall0)
        }
    }

    private fun initGame() {
        isPlayerTurn = true
        playerScore = 0
        computerScore = 0
    }

    private fun updateUI(tvTurn: TextView, tvCaller: TextView, radioGroupCall: RadioGroup, btnAction: Button) {
        if (isPlayerTurn) {
            tvTurn.text = "輪到玩家喊：請選擇喊的數字"
            tvCaller.text = "喊的人：玩家"
            btnAction.text = "玩家喊聲"
            // 解鎖喊的數字選擇
            for (i in 0 until radioGroupCall.childCount) {
                radioGroupCall.getChildAt(i).isEnabled = true
            }
        } else {
            tvTurn.text = "輪到電腦喊：你不用喊數字"
            tvCaller.text = "喊的人：電腦"
            btnAction.text = "電腦喊聲"
            // 鎖定喊的數字選擇
            for (i in 0 until radioGroupCall.childCount) {
                radioGroupCall.getChildAt(i).isEnabled = false
            }
        }
    }

    private fun playPlayerTurn(
        radioGroupNumber: RadioGroup,
        radioGroupCall: RadioGroup,
        tvPlayerResult: TextView,
        tvComputerResult: TextView,
        tvCallResult: TextView,
        tvTotalResult: TextView,
        tvScore: TextView,
        tvTurn: TextView,
        tvCaller: TextView
    ) {
        // 1. 取得玩家出的手指數
        val playerFingers = when (radioGroupNumber.checkedRadioButtonId) {
            R.id.btnNumber0 -> 0
            R.id.btnNumber5 -> 5
            R.id.btnNumber10 -> 10
            else -> 0
        }

        // 2. 取得玩家喊的數字
        val playerCall = when (radioGroupCall.checkedRadioButtonId) {
            R.id.btnCall0 -> 0
            R.id.btnCall5 -> 5
            R.id.btnCall10 -> 10
            R.id.btnCall15 -> 15
            R.id.btnCall20 -> 20
            else -> 0
        }

        // 3. 電腦隨機出手指數
        val computerFingers = fingerNumbers.random()

        // 4. 計算總和
        val total = playerFingers + computerFingers

        // 5. 顯示結果
        tvPlayerResult.text = "玩家出拳：\${getFingerText(playerFingers)} (\$playerFingers)"
        tvComputerResult.text = "電腦出拳：\${getFingerText(computerFingers)} (\$computerFingers)"
        tvCallResult.text = "本回合喊：玩家喊「\${getCallText(playerCall)}」"
        tvTotalResult.text = "總和：\$total"

        // 6. 判斷勝負
        if (total == playerCall) {
            // 玩家喊中，玩家得分
            playerScore++
            tvScore.text = "玩家喊中了！比分：玩家 \$playerScore - \$computerScore 電腦"
            // 玩家繼續喊（不換人）
            isPlayerTurn = true
        } else {
            // 玩家沒喊中，換電腦喊
            tvScore.text = "玩家沒喊中，換電腦喊。比分：玩家 \$playerScore - \$computerScore 電腦"
            isPlayerTurn = false
        }
    }

    private fun playComputerTurn(
        radioGroupNumber: RadioGroup,
        tvPlayerResult: TextView,
        tvComputerResult: TextView,
        tvCallResult: TextView,
        tvTotalResult: TextView,
        tvScore: TextView,
        tvTurn: TextView,
        tvCaller: TextView
    ) {
        // 1. 取得玩家出的手指數
        val playerFingers = when (radioGroupNumber.checkedRadioButtonId) {
            R.id.btnNumber0 -> 0
            R.id.btnNumber5 -> 5
            R.id.btnNumber10 -> 10
            else -> 0
        }

        // 2. 電腦隨機喊數字
        val computerCall = callNumbers.random()

        // 3. 電腦隨機出手指數
        val computerFingers = fingerNumbers.random()

        // 4. 計算總和
        val total = playerFingers + computerFingers

        // 5. 顯示結果
        tvPlayerResult.text = "玩家出拳：\${getFingerText(playerFingers)} (\$playerFingers)"
        tvComputerResult.text = "電腦出拳：\${getFingerText(computerFingers)} (\$computerFingers)"
        tvCallResult.text = "本回合喊：電腦喊「\${getCallText(computerCall)}」"
        tvTotalResult.text = "總和：\$total"

        // 6. 判斷勝負
        if (total == computerCall) {
            // 電腦喊中，電腦得分
            computerScore++
            tvScore.text = "電腦喊中了！比分：玩家 \$playerScore - \$computerScore 電腦"
            // 電腦繼續喊（不換人）
            isPlayerTurn = false
        } else {
            // 電腦沒喊中，換玩家喊
            tvScore.text = "電腦沒喊中，換玩家喊。比分：玩家 \$playerScore - \$computerScore 電腦"
            isPlayerTurn = true
        }
    }

    private fun getFingerText(fingers: Int): String {
        return when (fingers) {
            0 -> "0"
            5 -> "5"
            10 -> "10"
            else -> "未知"
        }
    }

    private fun getCallText(call: Int): String {
        return when (call) {
            0 -> "0"
            5 -> "5"
            10 -> "10"
            15 -> "15"
            20 -> "20"
            else -> "未知"
        }
    }
}
