// 使用版本目錄中定義的插件
plugins {
    alias(libs.plugins.android.application)  // Android 應用程式插件
    alias(libs.plugins.kotlin.android)       // Kotlin 支援插件
}

android {
    // 應用程式命名空間，用於區分不同應用
    namespace = "com.example.myapplication_0920"
    
    // 編譯時使用的 SDK 版本
    compileSdk {
        version = release(36)  // 使用 API 36 進行編譯
    }

    // 應用程式預設設定
    defaultConfig {
        applicationId = "com.example.myapplication_0920"  // 應用程式唯一識別碼
        minSdk = 33              // 最低支援 Android 13 版本
        targetSdk = 36          // 目標 Android 14 版本
        versionCode = 1         // 版本編號，用於更新判斷
        versionName = "1.0"     // 版本名稱，顯示給使用者看的版本號

        // 設定測試執行器
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    // 建置類型設定
    buildTypes {
        release {
            isMinifyEnabled = false  // 是否開啟程式碼壓縮，false 代表關閉
            proguardFiles(          // 程式碼混淆設定檔
                getDefaultProguardFile("proguard-android-optimize.txt"),  // 系統預設設定
                "proguard-rules.pro"                                     // 自訂設定
            )
        }
    }
    
    // Java 版本相容性設定
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11  // 原始碼使用 Java 11
        targetCompatibility = JavaVersion.VERSION_11  // 編譯後使用 Java 11
    }
    
    // Kotlin 編譯設定
    kotlinOptions {
        jvmTarget = "11"  // 設定 JVM 目標版本為 Java 11
    }
    
    // 建置功能開關
    buildFeatures {
        viewBinding = true  // 開啟 ViewBinding，可以更方便的操作介面元件
    }
}

// 專案相依套件設定
dependencies {
    implementation(libs.androidx.core.ktx)      // Android 核心函式庫，包含 Kotlin 擴充功能
    implementation(libs.androidx.appcompat)     // 向下相容支援函式庫
    implementation(libs.material)               // Material Design 介面設計元件
    implementation(libs.androidx.activity)      // Activity 元件
    implementation(libs.androidx.constraintlayout) // 靈活的佈局管理器
    testImplementation(libs.junit)              // 單元測試框架
    androidTestImplementation(libs.androidx.junit)  // Android 測試用的 JUnit
    androidTestImplementation(libs.androidx.espresso.core)  // UI 自動化測試框架
}