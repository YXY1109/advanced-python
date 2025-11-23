# 高级通知脚本
param(
    [string]$Message = "任务完成",
    [string]$Type = "completion"
)

Add-Type -AssemblyName System.Speech
Add-Type -AssemblyName System.Windows.Forms

try {
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

    # 根据类型设置不同的语音
    switch ($Type) {
        "notification" {
            $synth.Rate = 1  # 正常语速
            $sound = [System.Media.SystemSounds]::Hand
        }
        "completion" {
            $synth.Rate = 0  # 稍慢语速，更清晰
            $sound = [System.Media.SystemSounds]::Asterisk
        }
        "error" {
            $synth.Rate = 2  # 快速
            $sound = [System.Media.SystemSounds]::Exclamation
        }
        default {
            $synth.Rate = 0
            $sound = [System.Media.SystemSounds]::Asterisk
        }
    }

    # 播放系统声音
    $sound.Play()

    # 等待很短时间再播放语音
    Start-Sleep -Milliseconds 200

    # 语音播报
    $synth.Speak($Message)

} catch {
    Write-Host "通知播放失败: $_"
    # 即使失败也播放默认系统声音
    try {
        [System.Media.SystemSounds]::Beep.Play()
    } catch {
        # 完全失败时静默处理
    }
}