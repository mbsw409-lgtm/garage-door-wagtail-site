# Garage Door Supply House – Wagtail CMS Website

A responsive, CMS-driven website built with **Django** and **Wagtail** as a learning project. I recreated the structure and layout of an existing garage door retailer's website to practice building real-world page types, reusable content blocks and an editor-friendly admin.

> **Note:** This is a practice project and is not affiliated with the original business. Logos, product photos and brand assets are not included in this repository.

## Features

- **Home page** with a banner, content sections, cards, customer reviews, blog cards and an image row, all editable in Wagtail
- **Measuring page** using StreamField blocks (image + text sections that can be reordered)
- **Door Builder page** showing a grid of door cards; each door is a Wagtail snippet (name, image, prices, "on sale" option)
- **FAQ page** with Bootstrap accordions, with questions and answers managed in admin
- **Residential and Commercial pages**; Commercial includes a contact form built with Wagtail's form builder
- **Specials and Contact pages**, with Contact also using the form builder
- **Footer settings** (logos, headings, address) editable through Wagtail site settings
- Responsive layout with a sticky header and navigation, built on Bootstrap 5

## Tech stack

- Python, Django, Wagtail
- HTML, CSS, Bootstrap 5.3
- SQLite (development database)

## Run it locally

```bash
git clone https://github.com/YOUR-USERNAME/garage-door-wagtail-site.git
cd garage-door-wagtail-site

python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` for the admin. Pages are created in the admin (Pages → Home → Add child page); images are not included, so upload your own.

## What I learned

- Modelling content with Wagtail page types, snippets and StreamField blocks
- Keeping content in the CMS instead of hard-coding it into templates
- Building forms with Wagtail's form builder and storing submissions
- Matching a design with Bootstrap and custom CSS, and debugging CSS conflicts

## Known limitations

- Form submissions are saved in the admin, but email sending is not configured yet
- A few navigation pages (Our Advantage, Professional Installation, Gallery) are not built yet
- Development settings only; not deployed

## Author

**Muhammad** – Computer Science student, Lahore Leads University
