# Forest Run Website - Setup Guide

This repository contains a Hugo static site for Forest Run Collective with integrated booking forms and payment processing.

## 1. Getting Started Locally

### Prerequisites
- [Hugo](https://gohugo.io/installation/) v0.124.0+
- Git
- GitHub account
- Netlify account (free at netlify.com)

### Local Setup

```bash
# Clone the repo
git clone https://github.com/CWWhitney/forest-run-website.git
cd forest-run-website

# Start dev server
hugo server

# Open http://localhost:1313
```

The site will hot-reload as you make changes.

## 2. Install on GitHub

1. **Create repo on GitHub**:
   - Go to github.com/new
   - Name: `forest-run-website`
   - Make it Public
   - Don't initialize with README (we have one)

2. **Push to GitHub** (from your local folder):
   ```bash
   git init
   git add .
   git commit -m "Initial Forest Run website commit"
   git branch -M main
   git remote add origin https://github.com/CWWhitney/forest-run-website.git
   git push -u origin main
   ```

## 3. Deploy to Netlify

### Option A: Connect via Netlify Dashboard (Easiest)

1. **Go to netlify.com** → Sign in/Sign up
2. **Click "New site from Git"**
3. **Authorize GitHub** and select `forest-run-website` repository
4. **Build settings**:
   - Build command: `hugo --gc --minify`
   - Publish directory: `public`
5. **Deploy**
   - Netlify builds and deploys automatically
   - You'll get a `.netlify.app` URL

### Option B: Use Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy (from project folder)
netlify deploy --prod
```

## 4. Connect Your Domain (forestrun.org)

### Pointing Google Domains to Netlify

1. **In Netlify**:
   - Go to Site Settings → Domain management
   - Click "Add domain" and enter `forestrun.org`
   - Netlify will provide nameservers (e.g., `dns1.p.netlify.com`)

2. **In Google Domains**:
   - Go to your domain settings
   - Find "DNS" or "Custom nameservers"
   - Replace Google's nameservers with Netlify's nameservers
   - **Note**: This takes 24-48 hours to propagate

3. **Verify in Netlify**:
   - Once propagated, Netlify auto-generates an SSL certificate
   - Your site is now live at `https://forestrun.org`

## 5. Add Payment Processing

### Stripe Integration

1. **Create Stripe account** at stripe.com
2. **Get API keys**:
   - Go to Developers → API keys
   - Copy "Publishable key" & "Secret key"

3. **Add to Netlify environment variables**:
   - Netlify dashboard → Site settings → Build & deploy → Environment
   - Add:
     - `STRIPE_PUBLIC_KEY` = your publishable key
     - `STRIPE_SECRET_KEY` = your secret key (keep private!)

4. **Add payment buttons** to service pages:
   - Edit `content/services.md` or `content/bookings.md`
   - Add Stripe embed code (example below)

### PayPal Integration

1. **Create PayPal Business account** at paypal.com
2. **Get Merchant ID**:
   - Go to Account Settings → Business info
   - Note your Merchant Account ID

3. **Add to Netlify environment variables**:
   - `PAYPAL_MERCHANT_ID` = your merchant ID

4. **Add PayPal buttons** to pages:
   - Edit content files and add PayPal embed

## 6. Stripe Payment Button Example

Add this to any markdown page where you want a payment button:

```html
<script async src="https://js.stripe.com/v3/"></script>

<div id="payment-element"></div>
<button id="submit">Pay Now</button>

<script>
  // Initialize Stripe
  const stripe = Stripe('pk_live_YOUR_PUBLIC_KEY');
  const elements = stripe.elements();
  const paymentElement = elements.create('payment');
  paymentElement.mount('#payment-element');

  document.getElementById('submit').addEventListener('click', async () => {
    const result = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: 'https://forestrun.org/success/',
      },
    });
  });
</script>
```

## 7. Booking Form (Netlify Forms)

Forms are already integrated! Any `<form>` with `netlify` attribute automatically:
- Stores submissions in Netlify dashboard
- Sends email notifications
- Redirects to success page

**To receive booking emails**:
1. In Netlify: Site settings → Forms
2. Enable email notifications
3. Add your email address

## 8. Customization

### Edit Content
- All pages are in `content/` as markdown files
- Images go in `static/images/`
- Edit site settings in `config.toml`

### Style Changes
- Modify `static/css/style.css`
- Colors defined in `:root` variables

### Add New Pages
1. Create new markdown file in `content/`:
   ```bash
   hugo new content/my-page.md
   ```
2. Edit the file with your content
3. Add to navigation in `config.toml`
4. Push to GitHub (auto-deploys!)

## 9. Workflow for Future Changes

```bash
# Make changes locally
nano content/services.md

# Test locally
hugo server

# Commit and push
git add .
git commit -m "Update services pricing"
git push origin main

# Netlify auto-deploys! (1-2 minutes)
```

## 10. Troubleshooting

**Site not deploying?**
- Check Netlify Deploy logs: Netlify dashboard → Deploys
- Common issues:
  - Hugo version mismatch (set in `netlify.toml`)
  - Missing config.toml
  - Broken markdown syntax

**Domain not resolving?**
- DNS changes take 24-48 hours
- Check nameservers are correct: `dig forestrun.org`

**Forms not submitting?**
- Make sure form has `netlify` attribute and `name` attribute
- Not using `method="POST"` in older browsers? Try adding it

**Payment not working?**
- Check API keys are correct
- Verify keys are in Netlify environment variables
- Test with Stripe test mode first (use `pk_test_...` keys)

## 11. Monthly Maintenance

- **Week 1**: Review form submissions, follow up on bookings
- **Week 2**: Update availability calendar if needed
- **Week 3**: Check site analytics (in Netlify)
- **Week 4**: Review any issues, plan content updates

## Support

- Hugo docs: https://gohugo.io/documentation/
- Netlify docs: https://docs.netlify.com/
- Stripe docs: https://stripe.com/docs
- Questions? Email whitney.cory@gmail.com

---

**Happy deploying!** 🏃‍♀️🌲
