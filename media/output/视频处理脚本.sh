#!/bin/bash
# 视频处理脚本 - 竖屏转换 + 音效 + 电影感
# 使用方式：bash 视频处理脚本.sh

INPUT_VIDEO="/home/admin/.openclaw/workspace-chief-agent/media/inbound/video-1776165110002.mp4"
OUTPUT_DIR="/home/admin/.openclaw/workspace-chief-agent/media/output"
AUDIO_DIR="/home/admin/.openclaw/workspace-chief-agent/media/audio"

echo "🎬 开始视频处理..."
echo "输入：$INPUT_VIDEO"
echo "输出：$OUTPUT_DIR"

# 检查 ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg 未安装，请先安装"
    exit 1
fi

# 步骤 1: 转换为竖屏（9:16）
echo "📱 步骤 1: 转换为竖屏格式..."
ffmpeg -i "$INPUT_VIDEO" \
    -vf "scale=1080:1920:force_original_aspect_ratio=decrease,\
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,\
unsharp=5:5:1.0" \
    -c:v libx264 -preset medium -crf 23 \
    -c:a aac -b:a 128k \
    "$OUTPUT_DIR/video_vertical.mp4" \
    -y

# 步骤 2: 添加音效和背景音乐（如果有音频文件）
if [ -f "$AUDIO_DIR/horse_hooves.mp3" ] && [ -f "$AUDIO_DIR/happy_bgm.mp3" ]; then
    echo "🎵 步骤 2: 添加音效和背景音乐..."
    ffmpeg -i "$OUTPUT_DIR/video_vertical.mp4" \
        -i "$AUDIO_DIR/horse_hooves.mp3" \
        -i "$AUDIO_DIR/happy_bgm.mp3" \
        -filter_complex "[1:a][2:a]amix=inputs=2:duration=first:dropout_transition=2[a]" \
        -map 0:v -map "[a]" \
        -c:v libx264 -preset medium -crf 23 \
        -c:a aac -b:a 192k \
        "$OUTPUT_DIR/video_final.mp4" \
        -y
else
    echo "⚠️ 音效文件不存在，跳过音频混合步骤"
    cp "$OUTPUT_DIR/video_vertical.mp4" "$OUTPUT_DIR/video_final.mp4"
fi

echo "✅ 视频处理完成！"
echo "输出文件：$OUTPUT_DIR/video_final.mp4"
ls -lh "$OUTPUT_DIR/video_final.mp4"
