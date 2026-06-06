# Test Plan

**App:** https://www.saucedemo.com  
**Stack:** Playwright + Python  
**Pattern:** Page Object Model  
**Total test cases:** 37

This document covers all planned test cases for the SauceDemo app, grouped by feature area. Each case includes the goal, steps, and expected outcome. Cases marked ✅ are implemented; ⬜ are pending.

---

## Implementation status

| Group | Cases | Status |
|-------|-------|--------|
| Login | TC01 - TC07 | ✅ Done |
| Inventory | TC08 - TC13 | ✅ Done |
| Product details | TC14 - TC17 | ✅ Done |
| Cart | TC18 - TC23 | ✅ Done |
| Checkout - form | TC24 - TC27 | ✅ Done |
| Checkout - summary & order | TC28 - TC31 | ⬜ Pending |
| Logout & navigation | TC32 - TC35 | ⬜ Pending |
| Special users | TC36 - TC37 | ⬜ Pending |

---

## 1. Login - TC01 - TC07

---

### TC01 - Successful login with standard_user ✅

**Goal:** Verify that a standard user can log in and see the product list.

**Steps:**
1. Open `https://www.saucedemo.com`
2. Enter username: `standard_user`
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- URL changes to `/inventory.html`
- Header shows `Swag Labs`
- Product list contains at least one item

---

### TC02 - Login attempt with locked_out_user ✅

**Goal:** Verify that a locked account cannot log in and an error message is shown.

**Steps:**
1. Open the login page
2. Enter username: `locked_out_user`
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- Stays on the login page
- Error: `Epic sadface: Sorry, this user has been locked out`
- Error icons appear on both form fields

---

### TC03 - Login with wrong password ✅

**Goal:** Verify that incorrect credentials are properly rejected.

**Steps:**
1. Open the login page
2. Enter username: `standard_user`
3. Enter password: `wrong_password`
4. Click `Login`

**Expected result:**
- Stays on the login page
- Error: `Epic sadface: Username and password do not match`

---

### TC04 - Login with empty username and password ✅

**Goal:** Verify that submitting an empty form triggers validation.

**Steps:**
1. Open the login page
2. Leave both fields empty
3. Click `Login`

**Expected result:**
- Stays on the login page
- Error: `Epic sadface: Username is required`

---

### TC05 - Login with empty password ✅

**Goal:** Verify validation when username is filled but password is empty.

**Steps:**
1. Open the login page
2. Enter username: `standard_user`
3. Leave password empty
4. Click `Login`

**Expected result:**
- Error: `Epic sadface: Password is required`

---

### TC06 - Login with empty username ✅

**Goal:** Verify validation when password is filled but username is empty.

**Steps:**
1. Open the login page
2. Leave username empty
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- Error: `Epic sadface: Username is required`

---

### TC07 - Login with problem_user ✅

**Goal:** Verify that problem_user can log in despite known UI issues.

**Steps:**
1. Open the login page
2. Enter username: `problem_user`
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- URL changes to `/inventory.html`
- Product list is visible (regardless of image issues)

---

## 2. Inventory - TC08 - TC13

---

### TC08 - Product list displayed after login ✅

**Goal:** Verify the product list loads correctly after logging in.

**Steps:**
1. Log in as `standard_user`
2. Check the contents of `/inventory.html`

**Expected result:**
- Exactly 6 products are visible
- Each product has a name, description, price, and `Add to cart` button
- Prices are in `$X.XX` format

---

### TC09 - Sort products A to Z (default) ✅

**Goal:** Verify the default sort order is alphabetical ascending.

**Steps:**
1. Log in and go to the product list
2. Check the currently selected sort option
3. Read all product names

**Expected result:**
- Default sort is `Name (A to Z)`
- Names are in ascending alphabetical order

---

### TC10 - Sort products Z to A ✅

**Goal:** Verify reverse alphabetical sorting works.

**Steps:**
1. Log in and go to the product list
2. Select `Name (Z to A)` from the dropdown
3. Read all product names

**Expected result:**
- Names are in descending alphabetical order

---

### TC11 - Sort products by price ascending ✅

**Goal:** Verify sorting from cheapest to most expensive.

**Steps:**
1. Log in and go to the product list
2. Select `Price (low to high)` from the dropdown
3. Read all product prices

**Expected result:**
- Prices increase from first to last item

---

### TC12 - Sort products by price descending ✅

**Goal:** Verify sorting from most expensive to cheapest.

**Steps:**
1. Log in and go to the product list
2. Select `Price (high to low)` from the dropdown
3. Read all product prices

**Expected result:**
- Prices decrease from first to last item

---

### TC13 - Cart badge updates after adding a product ✅

**Goal:** Verify the cart icon counter updates when a product is added.

**Steps:**
1. Log in and go to the product list
2. Confirm the cart icon has no badge
3. Click `Add to cart` on the first product
4. Check the cart icon

**Expected result:**
- Before adding: no badge visible
- After adding: badge shows `1`

---

## 3. Product details - TC14 - TC17

---

### TC14 - Clicking a product name opens its details page ✅

**Goal:** Verify that clicking a product name navigates to the details page.

**Steps:**
1. Log in and go to the product list
2. Click the name of the first product

**Expected result:**
- URL changes to `/inventory-item.html?id=X`
- Product name, description, price, and image are visible
- `Add to cart` button is available

---

### TC15 - Adding a product from details page updates the cart badge ✅

**Goal:** Verify a product can be added to the cart from its details page.

**Steps:**
1. Navigate to any product's details page
2. Click `Add to cart`
3. Check the button state and cart badge

**Expected result:**
- Button changes to `Remove`
- Cart badge shows `1`

---

### TC16 - Removing a product from details page clears the cart badge ✅

**Goal:** Verify a product can be removed from the cart while on its details page.

**Steps:**
1. Navigate to any product's details page
2. Click `Add to cart`
3. Click `Remove`

**Expected result:**
- Button returns to `Add to cart`
- Cart badge disappears

---

### TC17 - Back to products button returns to inventory ✅

**Goal:** Verify the back button navigates back to the product list.

**Steps:**
1. Navigate to any product's details page
2. Click `Back to products`

**Expected result:**
- Returns to `/inventory.html`
- Product list is visible
- Cart state is unchanged

---

## 4. Cart - TC18 - TC23

---

### TC18 - Adding one product shows it in the cart with correct details ✅

**Goal:** Verify the basic add-to-cart flow.

**Steps:**
1. Log in and go to the product list
2. Click `Add to cart` on any product
3. Click the cart icon in the header

**Expected result:**
- URL changes to `/cart.html`
- Cart contains one product with name, description, price, and quantity `1`

---

### TC19 - Adding 3 products shows all of them in the cart ✅

**Goal:** Verify the cart correctly displays multiple products.

**Steps:**
1. Log in and add 3 different products
2. Go to the cart

**Expected result:**
- Cart badge shows `3`
- Cart contains exactly 3 products
- Each product has the correct name and price

---

### TC20 - Removing a product from cart leaves one item ✅

**Goal:** Verify product removal from the cart view.

**Steps:**
1. Add 2 products to the cart
2. Go to the cart
3. Click `Remove` on the first product

**Expected result:**
- Cart contains 1 product
- Cart badge updates to `1`
- Removed product is no longer listed

---

### TC21 - Removing the only product leaves the cart empty ✅

**Goal:** Verify the empty cart state.

**Steps:**
1. Add 1 product to the cart
2. Go to the cart
3. Click `Remove`

**Expected result:**
- Cart item list is empty
- Cart badge disappears
- `Checkout` button is still visible

---

### TC22 - Continue shopping returns to inventory with cart intact ✅

**Goal:** Verify the `Continue Shopping` button works correctly.

**Steps:**
1. Add a product and go to the cart
2. Click `Continue Shopping`

**Expected result:**
- Returns to `/inventory.html`
- Cart badge still shows the added product

---

### TC23 - Cart content survives a page reload ✅

**Goal:** Verify that the cart state is preserved across page reloads.

**Steps:**
1. Log in and add a product to the cart
2. Reload the page
3. Check the cart icon

**Expected result:**
- Cart badge still shows `1`
- Product is still in the cart at `/cart.html`

---

## 5. Checkout - form - TC24 - TC27

---

### TC24 - Clicking checkout opens the form with all required fields ✅

**Goal:** Verify the Checkout button navigates to the data entry form.

**Steps:**
1. Add a product and go to the cart
2. Click `Checkout`

**Expected result:**
- URL changes to `/checkout-step-one.html`
- Form fields visible: `First Name`, `Last Name`, `Zip/Postal Code`
- `Cancel` and `Continue` buttons are visible

---

### TC25 - Submitting checkout without first name shows an error ✅

**Goal:** Verify First Name field validation.

**Steps:**
1. Go to the checkout form
2. Leave `First Name` empty
3. Fill `Last Name`: `Kowalski`
4. Fill `Zip Code`: `00-000`
5. Click `Continue`

**Expected result:**
- Stays on `/checkout-step-one.html`
- Error: `Error: First Name is required`

---

### TC26 - Submitting checkout without last name shows an error ✅

**Goal:** Verify Last Name field validation.

**Steps:**
1. Go to the checkout form
2. Fill `First Name`: `Jan`
3. Leave `Last Name` empty
4. Fill `Zip Code`: `00-000`
5. Click `Continue`

**Expected result:**
- Error: `Error: Last Name is required`

---

### TC27 - Submitting checkout without postal code shows an error ✅

**Goal:** Verify Zip Code field validation.

**Steps:**
1. Go to the checkout form
2. Fill `First Name`: `Jan`
3. Fill `Last Name`: `Kowalski`
4. Leave `Zip Code` empty
5. Click `Continue`

**Expected result:**
- Error: `Error: Postal Code is required`

---

## 6. Checkout - summary & order - TC28 - TC31

---

### TC28 - Successfully complete checkout form ⬜

**Goal:** Verify that valid data moves the user to the order summary step.

**Steps:**
1. Add a product and go to checkout
2. Fill: `First Name`: `Jan`, `Last Name`: `Kowalski`, `Zip`: `00-001`
3. Click `Continue`

**Expected result:**
- URL changes to `/checkout-step-two.html`
- Order Summary section is visible
- Product list, unit price, tax, and total are shown

---

### TC29 - Verify order summary amounts ⬜

**Goal:** Verify that the amounts on the summary page add up correctly.

**Steps:**
1. Add 2 products (note their prices)
2. Go through checkout to the summary step
3. Check `Item total`, `Tax`, and `Total`

**Expected result:**
- `Item total` equals the sum of the added product prices
- `Total` equals `Item total` + `Tax`
- All values are in `$X.XX` format

---

### TC30 - Cancel on order summary page ⬜

**Goal:** Verify the Cancel button on the summary page.

**Steps:**
1. Navigate to the order summary page
2. Click `Cancel`

**Expected result:**
- Returns to `/inventory.html`
- Cart still contains the added products

---

### TC31 - Complete order and see confirmation screen ⬜

**Goal:** Verify the full purchase flow from start to finish.

**Steps:**
1. Log in as `standard_user`
2. Add a product to the cart
3. Go through checkout with valid data
4. Click `Finish` on the summary page

**Expected result:**
- URL changes to `/checkout-complete.html`
- Header shows `Thank you for your order!`
- `Back Home` button is visible
- Cart badge disappears

---

## 7. Logout & navigation - TC32 - TC35

---

### TC32 - Successful logout via sidebar menu ⬜

**Goal:** Verify a user can log out through the sidebar.

**Steps:**
1. Log in as `standard_user`
2. Open the burger menu in the top-left corner
3. Click `Logout`

**Expected result:**
- URL returns to `/` (login page)
- Login form is visible
- Session is ended

---

### TC33 - No access to /inventory after logout ⬜

**Goal:** Verify that a logged-out user cannot access protected pages.

**Steps:**
1. Log in, then log out
2. Try to navigate directly to `https://www.saucedemo.com/inventory.html`

**Expected result:**
- Redirected to the login page
- Product list is not accessible

---

### TC34 - Sidebar menu contains all expected options ⬜

**Goal:** Verify the sidebar menu content.

**Steps:**
1. Log in as `standard_user`
2. Open the burger menu
3. Check the available options

**Expected result:**
- Menu contains: `All Items`, `About`, `Logout`, `Reset App State`
- Menu can be closed with the `X` button

---

### TC35 - Reset app state via sidebar menu clears the cart ⬜

**Goal:** Verify that `Reset App State` empties the cart.

**Steps:**
1. Log in as `standard_user`
2. Add 2 products to the cart
3. Open the burger menu
4. Click `Reset App State`
5. Close the menu and check the cart

**Expected result:**
- Cart badge disappears
- Cart is empty
- `Add to cart` buttons on the product list are back to their default state

---

## 8. Special users - TC36 - TC37

---

### TC36 - performance_glitch_user logs in and reaches the inventory page ⬜

**Goal:** Verify that performance_glitch_user can log in despite intentionally slow response times.

**Steps:**
1. Open the login page
2. Enter username: `performance_glitch_user`
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- URL changes to `/inventory.html`
- Product list shows 6 items

---

### TC37 - error_user logs in and reaches the inventory page ⬜

**Goal:** Verify that error_user can log in and land on the inventory page.

**Steps:**
1. Open the login page
2. Enter username: `error_user`
3. Enter password: `secret_sauce`
4. Click `Login`

**Expected result:**
- URL changes to `/inventory.html`
- Product list shows 6 items

---

## Summary

| Group | Cases | Count |
|-------|-------|-------|
| Login | TC01 - TC07 | 7 |
| Inventory | TC08 - TC13 | 6 |
| Product details | TC14 - TC17 | 4 |
| Cart | TC18 - TC23 | 6 |
| Checkout - form | TC24 - TC27 | 4 |
| Checkout - summary & order | TC28 - TC31 | 4 |
| Logout & navigation | TC32 - TC35 | 4 |
| Special users | TC36 - TC37 | 2 |
| **Total** | | **37** |
