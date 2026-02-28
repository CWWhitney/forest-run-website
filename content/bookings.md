---
title: "Book an Experience"
description: "Reserve"
draft: false
---

## Book Your Forest Run Experience

Welcome to Forest Run Collective! Reserve our sauna

### How to Book

2. Fill out the booking request form
3. We'll confirm your booking and send payment details by email

---

## Available Services & Pricing

**Sauna & Wellness**
- Open Sauna Hours: $35/person (1 hour)
- Private Sauna Session: $180/group of 5+ (1 hour)

---

## Booking Request Form

<form name="booking-inquiry" method="POST" action="/success/" netlify>
  <p>
    <label>Service: <select name="service-type" required>
      <option value="">-- Select --</option>
      <option value="sauna-session">Sauna & Wellness Session</option>
      <option value="sauna-workshop">Wellness Workshop</option>
      <option value="cabin-rental">Cabin Rental</option>
      <option value="camping">Camping</option>
      <option value="training-camp">Training Camp</option>
      <option value="guided-run">Guided Run</option>
    </select></label>
  </p>
  <p>
    <label>Preferred Date: <input type="date" name="date" required></label>
  </p>
  <p>
    <label>Number of Guests: <input type="number" name="num-guests" min="1" max="20" value="1" required></label>
  </p>
  <p>
    <label>Your Name: <input type="text" name="name" required></label>
  </p>
  <p>
    <label>Email: <input type="email" name="email" required></label>
  </p>
  <p>
    <label>Special Requests or Questions:<br>
    <textarea name="message" rows="4"></textarea></label>
  </p>
  <p>
    <button type="submit">Submit Booking Request</button>
  </p>
</form>

---

**Questions?** Email {{< param bookings_email >}}

**Cancellation Policy:** Free cancellation up to 14 days before your booking.

