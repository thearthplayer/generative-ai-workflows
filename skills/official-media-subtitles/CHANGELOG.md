# 更新记录 / Changelog

## 1.0.0 — 2026-09-15

首次为公开字幕 Skill 建立版本基线。此前公开发布的未编号版本与此版本使用相同的字幕处理规则和校验脚本。

### 本次新增 / Added
- VERSION 文件，以及 SKILL.md 的 metadata.version。
- 首页版本标记、版本号约定、使用者升级指令和回退方法。
- 明确区分 Git 仓库副本更新与 WorkBuddy 已安装副本更新。

### 功能与依赖 / Behavior and dependencies
- 字幕编辑规则、时间轴原则和 Python 校验逻辑没有改变。
- 不捆绑语音转写引擎；Python 3 和可选 ffprobe 的要求不变。
- 未配置自动检查更新或后台安装。

### 从未编号版本升级 / Migration
先比较已安装文件，备份本地修改，再完整安装新版。缺少 VERSION 表示未标记版本，不代表技能损坏。

### 验证范围 / Validation
技能结构检查通过；首次公开版的校验器已通过有效 SRT、禁用标点和时间重叠测试。本次只增加版本信息与文档，没有新增音视频业务测试；WorkBuddy 中的实际识别与转写效果仍需使用者验证。

## 未编号公开版 / Unversioned public snapshot — 2026-09-15

- 首次公开通用字幕编辑规则、SRT 校验脚本和安装说明。
- 去除具体节目名称、审核日期与采访原话案例。
- 初次发布提交：[966b3f8](https://github.com/thearthplayer/generative-ai-workflows/commit/966b3f833061961b44e593a6bfabd0e51fbfe238)。
