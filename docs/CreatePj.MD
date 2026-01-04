## `cd yaru`

## `md backend, frontend, docker, docs`

```
New-Item .gitignore -ItemType File
New-Item docker-compose.yml -ItemType File
```

---

## `npx create-next-app@latest frontend`

## `cd backend`

## `python -m venv venv`

## `New-Item main.py, requirements.txt -ItemType File`

## `mkdir app\api\v1, app\core, app\models, app\schemas, app\services\ai, app\services\vector, app\workers, alembic, tests`

```
New-Item requirements.txt, main.py, Dockerfile -ItemType File

New-Item app\api\deps.py -ItemType File
New-Item app\api\v1\auth.py, app\api\v1\videos.py, app\api\v1\learning.py, app\api\v1\vocab.py, app\api\v1\gamification.py, app\api\v1\quiz.py, app\api\v1\search.py -ItemType File

New-Item app\core\config.py, app\core\security.py, app\core\celery_app.py -ItemType File

New-Item app\models\user.py, app\models\video.py, app\models\transcript.py, app\models\vocabulary.py -ItemType File

New-Item app\schemas\video.py, app\schemas\transcript.py, app\schemas\user.py -ItemType File

New-Item app\services\ai\whisper_svc.py, app\services\ai\nlp_svc.py, app\services\ai\llm_svc.py -ItemType File
New-Item app\services\vector\openai_emb.py, app\services\vector\qdrant_svc.py -ItemType File
New-Item app\services\srs_algo.py, app\services\export_svc.py -ItemType File

New-Item app\workers\video_tasks.py -ItemType File

Get-ChildItem -Recurse -Directory | ForEach-Object { New-Item "$($_.FullName)\__init__.py" -ItemType File -ErrorAction SilentlyContinue }
```

---

## `cd ../frontend`

```
mkdir "app/(auth)", "app/(dashboard)/videos", "app/(dashboard)/vocab"
mkdir "app/watch/[videoId]", "app/practice/shadowing", "app/practice/dictation"
mkdir "components/ui", "components/player", "components/gamification", "components/community", "components/shared"
mkdir "lib/hooks", "store", "types", "public"

New-Item "app/(dashboard)/page.tsx", "app/watch/[videoId]/page.tsx", "app/globals.css", "app/layout.tsx" -ItemType File

New-Item "components/community/CommunitySection.tsx" -ItemType File
New-Item "components/player/VideoPlayer.tsx", "components/player/TranscriptList.tsx", "components/player/SubtitleOverlay.tsx", "components/player/FuriganaWord.tsx", "components/player/QuizPopup.tsx" -ItemType File

New-Item "lib/axios.ts", "lib/utils.ts", "lib/hooks/useVideoTime.ts", "lib/hooks/useAudioRecorder.ts" -ItemType File

New-Item "store/useUserStore.ts", "store/usePlayerStore.ts" -ItemType File
New-Item "types/video.d.ts", "types/api.d.ts" -ItemType File

New-Item "tailwind.config.ts", "package.json" -ItemType File
```
