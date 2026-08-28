# Codex skills collection

Практическая коллекция из 34 навыков для Codex: дизайн интерфейсов, анимация,
frontend-разработка, типографика, SEO и контроль качества.

## Быстрый выбор

| Задача | Рекомендуемые навыки |
| --- | --- |
| Создать или улучшить интерфейс | `ui-ux`, `frontend-design`, `refero-design`, `taste-skill` |
| Проверить качество UI | `frontend-ui-standards`, `web-design-guidelines`, `site-delivery-qa` |
| Спроектировать выразительный сайт | `build-awwwards-quality-sites`, `composition-patterns` |
| Добавить или проверить анимацию | `animate`, `find-animation-opportunities`, `review-animations` |
| Работать с GSAP | `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline` |
| Улучшить типографику | `typography`, `typography-audit`, `word-style-system` |
| Разрабатывать на React или Astro | `react-best-practices`, `astro-framework` |
| Провести SEO-аудит | `seo` |
| Автоматизировать браузер | `playwright` |

## Каталог

### Дизайн и интерфейсы

- `birman-interface-layout` — сценарная логика и пространственная ясность интерфейсов.
- `composition-patterns` — масштабируемая композиция React-компонентов.
- `emil-design-eng` — полировка UI и инженерный подход к деталям.
- `frontend-design` — выразительные production-ready интерфейсы.
- `frontend-ui-standards` — стандарты реализации и ревью UI.
- `gorbunov-ui-layout` — типографическая и модульная компоновка.
- `refero-design` — продуктовый и веб-дизайн на основе референсов.
- `superdesign` — работа с дизайном на холсте Superdesign.
- `taste-skill` — защита frontend-дизайна от шаблонности.
- `ui-ux` — основной контроль качества UI/UX.
- `web-design-guidelines` — аудит интерфейсов и доступности.

### Анимация

- `animate` — проектирование анимации с нуля.
- `animation-vocabulary` — поиск точного названия нужного motion-эффекта.
- `find-animation-opportunities` — поиск уместных мест для анимации.
- `improve-animations` — аудит и план улучшения motion-кода.
- `motion-gsap-lenis` — Motion.dev, GSAP и Lenis.
- `review-animations` — строгое ревью анимации.
- `gsap-core`, `gsap-frameworks`, `gsap-performance`, `gsap-plugins` — основа и оптимизация GSAP.
- `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-utils` — специализированные сценарии GSAP.

### Разработка, контент и контроль качества

- `astro-framework` — разработка на Astro.
- `build-awwwards-quality-sites` — выразительные маркетинговые и портфолио-сайты.
- `playwright` — браузерная автоматизация.
- `react-best-practices` — производительность React и Next.js.
- `seo` — технический и контентный SEO-аудит.
- `site-delivery-qa` — цикл реализации и визуального QA.
- `typography` — типографические решения.
- `typography-audit` — системный аудит веб-типографики.
- `word-style-system` — интерфейсные правила для Word-подобных сервисов.

## Установка

Скопируйте нужную папку навыка в каталог навыков Codex:

```bash
cp -R ui-ux ~/.codex/skills/
```

Перед использованием всей коллекции запустите быструю проверку:

```bash
python3 scripts/validate_skills.py
```

Навыки независимы: устанавливайте только те, которые нужны для текущей работы,
чтобы автоматический выбор оставался быстрым и точным.
