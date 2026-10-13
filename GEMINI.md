# GEMINI.md - Chợ Xanh AI Sale OS

## Vibe Builder Project Reference

### ⛔ CONTEXT OVERFLOW RECOVERY
**When context gets full or you feel lost in a long session:**
1. Re-read the vibe-builder skill: `.gemini/skills/vibe-builder/SKILL.md`
2. Re-read `IMPLEMENTATION_PLAN.md` to check current progress
3. Re-read `TEST_PLAN.md` (if exists) to check test status
4. Follow the workflow strictly - especially the checkpoints below!

### ⚠️ WORKFLOW CHECKPOINTS (MANDATORY - DO NOT SKIP!)
| After Phase | Action |
| --- | --- |
| Phase 3 (Coding) complete | → Create TEST_PLAN.md → **⛔ STOP for Human review** |
| Phase 4 (Test Plan) approved | → Execute tests autonomously |
| Phase 5 (Testing) complete | → Report results → Enter Phase 6 loop |

**CRITICAL:** After finishing ALL coding tasks, you MUST:
1. Create TEST_PLAN.md
2. **⛔ STOP and wait for Human approval**
3. DO NOT run any tests until Human reviews TEST_PLAN.md!

### Project Summary
- **App Type**: Web SaaS Platform (Multi-role, 4 Actors)
- **Tech Stack**: TypeScript + Next.js 14 + Supabase + TailwindCSS + Gemini API
- **4 Actors**:
  1. 🌾 **Thành viên HTX** – Mobile app: chụp ảnh, AI đăng SP, nhật ký canh tác
  2. 👨‍💼 **Quản lý HTX** – Dashboard: duyệt SP, Order Hub, AI Content, báo cáo
  3. 🏛️ **Cán bộ xã** – Read-only: báo cáo tổng hợp, xếp hạng HTX, OCOP tracking
  4. 🛒 **Người mua / Đối tác** – Public QR trace + B2B portal đặt đơn sỉ
- **Current Phase**: Phase 1 ✅ Done → Chờ Human approval để bắt đầu code

### Primary Documentation
- `PRD.md` - Full product requirements (lazy-read sections when needed)
- `IMPLEMENTATION_PLAN.md` - Task tracking with checkboxes
- `TEST_PLAN.md` - Test cases and results (created in Phase 4)

### Coding Guidelines
- Follow `IMPLEMENTATION_PLAN.md` for tasks
- Use TypeScript with strict mode
- Mark completed tasks with `[x]`
- Keep code minimal and focused
- Vietnamese UI text throughout the app
