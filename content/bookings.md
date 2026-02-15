---
title: "Book an Experience"
description: "Reserve your Forest Run experience. Running, sauna wellness, or overnight lodging."
draft: false
---

## Browse & Book

Use the calendar below to check availability and make your reservation.

<div class="booking-container">
  
  ### Select Your Service
  
  <form name="booking-inquiry" method="POST" action="/success/" netlify>
    
    <div class="form-group">
      <label for="service-type">What would you like to book?</label>
      <select name="service-type" id="service-type" required>
        <option value="">-- Select --</option>
        <option value="guided-run">Guided Run</option>
        <option value="sauna-session">Sauna & Wellness Session</option>
        <option value="cabin-rental">Cabin Rental</option>
        <option value="camping">Camping</option>
        <option value="workshop">Wellness Workshop</option>
        <option value="training-camp">Training Camp</option>
      </select>
    </div>

    <div class="form-group">
      <label for="date">Preferred Date</label>
      <input type="date" name="date" id="date" required>
    </div>

    <div class="form-group">
      <label for="num-guests">Number of Guests</label>
      <input type="number" name="num-guests" min="1" max="20" value="1" required>
    </div>

    <div class="form-group">
      <label for="name">Your Name</label>
      <input type="text" name="name" id="name" required>
    </div>

    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" name="email" id="email" required>
    </div>

    <div class="form-group">
      <label for="phone">Phone</label>
      <input type="tel" name="phone" id="phone">
    </div>

    <div class="form-group">
      <label for="message">Special Requests or Questions</label>
      <textarea name="message" id="message" rows="4"></textarea>
    </div>

    <button type="submit" class="btn btn-primary">Submit Booking Request</button>
  </form>

</div>

<div class="payment-info">
  
  ### Payment
  
  We accept payments via:
  - **Credit Card** (Stripe)
  - **PayPal**
  - **Direct Bank Transfer**
  
  After you submit your booking request, we'll send you a payment link. A $50 deposit reserves your spot; final payment is due 7 days before your experience.
  
  **Cancellation Policy**: Free cancellation up to 14 days before your booking. Deposits are non-refundable within 7 days.

</div>

### Questions?

Call us at {{< param phone >}} or email {{< param email >}}

Hours: Tuesday-Saturday, 9am-5pm ET
