# 📄 Deep Dive: dashboard.html (The "UI")

**Role**: The Interface. It combines structure (HTML), style (CSS), and logic (Jinja/JS).

## Key Sections Explained

### 1. The Head & Meta Tags (Line 6-7)
```html
<meta http-equiv="refresh" content="5">
```
*   **The Auto-Refresher**: This simple line tells the browser "Hit the F5 key automatically every 5 seconds".
*   This creates the "Real-Time" effect without needing complex WebSockets code.

### 2. CSS Variables (The Theme System) (Line 11-20)
```css
:root {
    --bg-color: #0a0e17;
    --accent-red: #ff3860;
}
```
*   We define our color palette here.
*   **Benefit**: If you want to change the red used for anomalies, you change it *here once*, and it updates:
    *   The border of the Red Cards.
    *   The text of the Anomaly rows.
    *   The badges in the status column.

### 3. The Grid System (Line 73-78)
```css
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```
*   **Responsive Design**:
    *   `minmax(200px, 1fr)`: Says "Cards must be at least 200px wide. If there's extra space, stretch them equally (`1fr`)."
    *   This ensures the dashboard looks good on both giant monitors and small laptops.

### 4. Jinja Logic (Line 230-245)
```html
{% for f in flights %}
    <tr class="{% if f.final_anomaly == 1 %}anomaly-row{% endif %}">
```
*   **Conditional Classing**:
    *   We check `f.final_anomaly` inside the `class="..."` attribute.
    *   If it's an anomaly, we add the class `anomaly-row`.
    *   CSS interacts with this: `.anomaly-row { color: var(--accent-red); }`.
    *   This is how specific rows turn red dynamically based on data.

### 5. Chart.js Data Injection (Line 252-253)
```html
const speeds = {{ flights[:20] | map(attribute='speed') | list | tojson }};
```
*   **The Problem**: Python has lists `[1, 2]`. JavaScript has arrays `[1, 2]`. They look similar but have subtle differences (like `None` vs `null`).
*   **The Solution**: `tojson` converts the Python data into a perfect JavaScript string.
*   **Integration**: We pass this data array directly into `new Chart(ctx, { data: speeds })`. This draws the line.
