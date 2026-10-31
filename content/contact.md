---
title: "Contact"
description: "Contact Forest Run Collective LLC in Camden, Maine."
draft: false
---

Forest Run Collective LLC, Emery Way, Camden, Maine 04843.

Use the form or write to {{< param email >}}.

<div class="contact-form">
<form name="contact" method="POST" netlify>
  <div class="form-group"><label for="name">Name</label><input type="text" name="name" id="name" required></div>
  <div class="form-group"><label for="email">Email</label><input type="email" name="email" id="email" required></div>
  <div class="form-group"><label for="subject">Subject</label><select name="subject" id="subject" required><option value="">Choose one</option><option value="visit">Visit or sauna</option><option value="project">Project question</option><option value="other">Other</option></select></div>
  <div class="form-group"><label for="message">Message</label><textarea name="message" id="message" rows="6" required></textarea></div>
  <button type="submit" class="btn btn-primary">Send message</button>
</form>
</div>
