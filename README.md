# Introduction

本工具旨在全平台地支持（Win/Mac/Linux）:
* 1.自动根据文件名将已有的视频文件夹里面的视频文件与字幕文件夹里面的字幕文件相匹配。
* 2.并将字幕文件夹里面的字幕名字改为与其对应视频的名称。

# Example

### 1.在视频文件夹中原有文件:
* [VCB-Studio] Uchinoko [01][Ma10p_1080p][x265_flac_aac][DsrtAS].mkv
* [VCB-Studio] Uchinoko [02][Ma10p_1080p][x265_flac][D(DAsmiSHDA)].mkv
* [VCB-Studio] Uchinoko [03][Ma10p_1080p][x265_flac][dasCOassP312].mkv

### 2.在字幕文件夹中原有文件:
* 為了女兒，我說不定連魔王都能幹掉。_1_繁體中文.srt
* 為了女兒，我說不定連魔王都能幹掉。_02_繁體中文.srt
* 為了女兒，我說不定連魔王都能幹掉。_3_繁體中文.srt

### 3.运行脚本
Windows用户可以直接运行可执行文件：字幕重命名工具_Win
Mac用户可以直接运行可执行文件：字幕重命名工具_Mac
Linux用户可以直接运行可执行文件：字幕重命名工具_Linux

#### 自己编译运行：
python3 rename_v2.py

### 4.根据提示输入视频文件夹以及字幕文件夹的绝对路径

### 5.运行结束后，字幕文件夹中的字幕名变为：

* 為了女兒，我說不定連魔王都能幹掉。_1_繁體中文.srt  更改为：  <br/>
  [VCB-Studio] Uchinoko [01][Ma10p_1080p][x265_flac_aac][DsrtAS].srt
* 為了女兒，我說不定連魔王都能幹掉。_02_繁體中文.srt 更改为：  <br/>
  [VCB-Studio] Uchinoko [02][Ma10p_1080p][x265_flac][D(DAsmiSHDA)].srt
* 為了女兒，我說不定連魔王都能幹掉。_3_繁體中文.srt  更改为：  <br/>
  [VCB-Studio] Uchinoko [03][Ma10p_1080p][x265_flac][dasCOassP312].srt

### 6.从而达到讲字幕文件与视频文件相对应的目的，这是讲字幕文件全部复制到视频文件夹中，播放视频就会自动带上字幕了。


# Usage

python3 rename_v2.py

# format support
ass/srt/ssa/sub/smi