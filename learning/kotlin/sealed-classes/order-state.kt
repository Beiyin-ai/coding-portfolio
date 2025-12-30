// Kotlin Sealed Class 學習範例：訂單狀態管理

// 1. 定義 sealed class OrderState
sealed class OrderState

object Created : OrderState()

data class Paid(val payType: PayType) : OrderState()

data class Shipped(
    val logisticsCompany: String,
    val trackingCode: String
) : OrderState()

object Finished : OrderState()

data class Cancelled(val reason: String) : OrderState()

// 2. 定義 enum class PayType
enum class PayType {
    CREDIT_CARD,
    LINE_PAY,
    APPLE_PAY
}

// 3. 撰寫函式 showState()
fun showState(state: OrderState): String {
    return when (state) {
        is Created -> "Order created"
        is Paid -> "Paid: Payment method: ${when (state.payType) {
            PayType.CREDIT_CARD -> "Credit Card"
            PayType.LINE_PAY -> "LINE Pay"
            PayType.APPLE_PAY -> "Apple Pay"
        }}"
        is Shipped -> "Shipped: Logistics company: ${state.logisticsCompany} | Tracking code: ${state.trackingCode}"
        is Finished -> "Order completed"
        is Cancelled -> "Order cancelled: Reason: ${state.reason}"
    }
}

// 4. 在 main() 中測試
fun main() {
    val states = listOf(
        Created,
        Paid(PayType.CREDIT_CARD),
        Shipped("Black Cat Express", "T123456789"),
        Cancelled("User requested cancellation"),
        Finished
    )

    println("=== Kotlin Sealed Class 範例 ===")
    states.forEach { state ->
        println(showState(state))
    }
}
