# Forest Run Collective Website

Welcome to the Forest Run Collective website repository. This is a Hugo static site deployed on Netlify.

## Getting Started

### Prerequisites
- [Hugo](https://gohugo.io/installation/) (v0.124.0 or later)
- Git

### Local Development

1. Clone the repo
   ```bash
   git clone https://github.com/YOUR-USERNAME/forest-run-website.git
   cd forest-run-website
   ```

2. Start the Hugo development server
   ```bash
   hugo server
   ```

3. Open `http://localhost:1313` in your browser

### Building

Build the site for production:
```bash
hugo --gc --minify
```

This creates the `public/` folder, which Netlify automatically deploys on git push.

## File Structure

- `content/` - All page content (markdown files)
- `static/` - Static files (images, PDFs, CSS)
- `layouts/` - HTML templates
- `config.toml` - Site configuration
- `netlify.toml` - Netlify build configuration

## Bookings & Payments

### Booking Form
- Uses Netlify Forms (backend: `/bookings/`)
- Customers submit booking requests
- You receive email notifications

### Payment Integration
- Stripe payment button on service pages
- PayPal button as fallback
- See `layouts/_default/services.html` for implementation

## Deployment

This site auto-deploys to Netlify on every push to `main` branch.

1. Connect repo to Netlify
2. Set build command: `hugo --gc --minify`
3. Set publish directory: `public`
4. Connect custom domain: `forestrun.org`

## License

MIT License
