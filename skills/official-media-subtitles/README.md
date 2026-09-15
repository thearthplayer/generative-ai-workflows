# 官方媒体中文字幕 / Official Media Chinese Subtitles

**当前公开版本 / Current public version: 1.0.0** · 2026-09-15

查看 [更新记录 / Changelog](CHANGELOG.md)；安装后读取技能文件夹中的 [VERSION](VERSION) 确认本地版本。版本号不保证文件未被本地修改。

把音视频制作、校对为忠实原声、时间码准确的中文 SRT 字幕。保留原意、立场、有信息量的重复和自我修正，列出听不清或无法确认的内容。

Create and proofread Chinese SRT subtitles faithful to the original speech and source timeline. Preserve meaning, stance, meaningful repetition and self-correction, and report unresolved uncertainties.

## 从 GitHub 安装到 WorkBuddy

把下面整段复制给 WorkBuddy：

```text
请从这个公开 GitHub 仓库安装“官方媒体中文字幕”技能：
https://github.com/thearthplayer/generative-ai-workflows

只安装子目录 skills/official-media-subtitles。
先读取该目录的 README.md、SKILL.md 和脚本，再确认当前版本 WorkBuddy 的个人技能目录。
完整下载这个子目录及其 scripts、references、agents 文件夹。
若同名技能已存在，先比较差异，不直接覆盖；有需要替换的内容时先保留旧版。
安装后确认技能能被应用识别，并检查 Python 3、ffprobe、本地语音转写和音频复听能力。
列明缺少的依赖，不把复制文件成功当成字幕生成功能已经全部可用。
不要执行仓库其它目录中的工作流，也不要要求我提供 GitHub 密码或令牌。
```

公开仓库读取不需要仓库访问授权。如果无法连接 GitHub，先解决网络问题；不要将下载失败误判为技能不兼容。

## Git 命令方式

想亲自验证 Git 下载，可在一个没有同名文件夹的工作目录运行：

```bash
git clone https://github.com/thearthplayer/generative-ai-workflows.git
cd generative-ai-workflows
```

技能位于 `skills/official-media-subtitles/`。让 WorkBuddy 完整安装这个文件夹，或在应用支持的本地技能导入入口导入它。文件夹与 `SKILL.md` 的英文名称保持不变。

更新时，在未修改的克隆目录运行 `git pull --ff-only`，再比较并更新已安装副本。克隆目录有本地修改或发生冲突时先停下处理，勿强制覆盖。Git 拉取更新不会自动更新 WorkBuddy 已安装的副本。

## 使用示例与依赖

安装后提供一小段有权使用的音视频和背景资料，再说：

> 使用官方媒体中文字幕技能，制作中文 SRT，保留原声时间轴，列出所有待确认项。

- 本包提供指令、编辑规则和 Python 校验器，**不包含语音识别模型或转写引擎**。
- 从媒体生成字幕需要宿主具备音视频读取、本地转写、时间戳及复听能力。缺少这些能力时，应明确报告限制；不自动将素材发送给外部转写服务。
- 校验脚本需要 Python 3；使用 `--media` 检查媒体时长还需要 FFmpeg 提供的 `ffprobe`。
- `agents/openai.yaml` 是可选的 Codex 界面信息，不是 WorkBuddy 工具能力的来源。
- 本技能默认字幕正文不含中英文逗号、句号，这是此编辑流程的约定，不是所有媒体通用的字幕标准。

```bash
python3 scripts/validate_srt.py example.srt --forbid-commas-periods
python3 scripts/validate_srt.py example.srt --media example.mp4 --forbid-commas-periods
```

脚本通过只说明所检查的结构和时间条件通过，不证明听写准确。应用识别与真实音频任务仍需单独试用。

## 公开版说明

此目录为主动发布的公开副本。已去除具体节目名称、审核日期和采访案例原话，保留通用编辑原则。私有备份不会因公开本目录而开放，其它个人和项目 Skills 不在本次发布范围。

## English installation notes

Clone this public repository and install only `skills/official-media-subtitles` into your agent's verified skill directory. Preserve the complete folder, including scripts and references. Compare existing copies before replacement. This package does not include an ASR engine; Python 3 is needed for validation, and ffprobe for media-duration checks. Verify skill recognition and test a short authorized audio sample before routine use.

## 版本与更新 / Versions and updates

这是首次编号的公开版 **1.0.0**。先前下载的无版本文件按“未标记版本”处理，不能仅凭没有 VERSION 判断内容过旧；先比较文件。WorkBuddy 是否在界面显示版本取决于应用支持，本包不依赖该显示功能。

版本使用“主版本.次版本.修订号”：
- 修订号（如 1.0.1）：兼容的错误修复、小幅提示词或说明优化。
- 次版本（如 1.1.0）：兼容地增加功能、可选能力或工作流程。
- 主版本（如 2.0.0）：改变默认编辑规则、输出约定或运行依赖，可能需要使用者调整流程。

`VERSION` 是发布版本依据；`SKILL.md` 中的 `metadata.version` 与首页版本同步维护。发布者每次发版应同时更新三处和 CHANGELOG，记录改动、依赖影响、迁移步骤与已完成的验证。发布后不要复用同一版本号承载新的修改；用 Git 提交 SHA 定位确切快照。

### 给 WorkBuddy 的更新指令

```text
请检查我安装的 official-media-subtitles 是否有新版。
公开仓库：https://github.com/thearthplayer/generative-ai-workflows
技能子目录：skills/official-media-subtitles

先读取已安装副本的 VERSION，再从公开仓库读取 VERSION 和 CHANGELOG.md。
无版本文件标记为“未标记”，不要猜版本。远端无法读取时报告检查失败，不要说已经最新。
有新版时说明变化，尤其是默认规则和依赖变化。比较本地文件，保留我的修改；遇到冲突先让我选择。
确认可更新后先备份旧技能文件夹，再完整更新此技能及其脚本、参考文件。
更新后核对 VERSION、metadata.version、文件完整性和应用识别状态，报告旧版、新版与来源提交 SHA。
如本地和远端版本号相同但内容不同，报告本地修改或版本不一致，不要强行覆盖。
不要更新仓库中其它技能或工作流。
```

Git 下载者可以在干净的克隆目录执行 `git pull --ff-only`；之后仍需更新 WorkBuddy 安装目录中的副本。ZIP 下载者需要重新下载新版。这两种方式均未配置后台自动检查或自动安装。

如新版不适合：保留新版副本，将升级前备份恢复到原安装位置，刷新技能列表并核对版本。需要历史公开快照时，在 GitHub 的文件历史/提交记录中选择对应提交，不要将整个仓库回退来替换单个技能。

### 发布者的操作约定

本地优化先保存到私有备份；公开发布仍由作者明确指定。发布前检查内部案例、个人路径和凭据，保留公开版的脱敏处理。更新公开版不会自动开放私有仓库，也不会自动更新其他人的安装副本。

### English

Read VERSION in the installed skill folder to identify its declared version. Review CHANGELOG before upgrading. Compare local modifications, back up the old folder, update the complete skill, and verify both the version and agent recognition. Git pull updates the clone, not a separately installed copy. ZIP installations require a new download. No automatic updater is configured. Keep the source commit SHA for an exact snapshot and use the local backup for rollback.
