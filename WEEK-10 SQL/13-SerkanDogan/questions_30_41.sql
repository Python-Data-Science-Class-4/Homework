-- SELECT AVG(film.length) AS average_duration
-- FROM film
-- JOIN film_category ON film.film_id = film_category.film_id
-- JOIN category ON film_category.category_id = category.category_id
-- WHERE category.name = 'Action';

-- SELECT store_id, COUNT(staff_id) AS staff_count
-- FROM staff
-- GROUP BY store_id
-- ORDER BY staff_count DESC
-- LIMIT 2;

-- SELECT film.film_id, film.title, film.rating
-- FROM actor
-- JOIN film_actor ON actor.actor_id = film_actor.actor_id
-- JOIN film ON film_actor.film_id = film.film_id
-- WHERE actor.first_name = 'Gene' AND actor.last_name = 'Willis';

-- SELECT COUNT(*) AS active_customers
-- FROM customer
-- WHERE active = 1;

-- SELECT film_id, title
-- FROM film
-- WHERE title LIKE 'C%';

-- SELECT DISTINCT customer.customer_id, customer.first_name, customer.last_name, customer.email
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- WHERE payment.amount < 4;

-- SELECT customer.first_name, customer.last_name, customer.customer_id
-- FROM customer
-- JOIN address ON customer.address_id = address.address_id
-- JOIN city ON address.city_id = city.city_id
-- WHERE city.city = 'Moscow';

-- SELECT staff.first_name, staff.last_name
-- FROM staff
-- JOIN address ON staff.address_id = address.address_id
-- JOIN city ON address.city_id = city.city_id
-- WHERE city.city = 'Moscow';

-- SELECT film.title, COUNT(rental.inventory_id) AS rental_count
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id
-- GROUP BY film.title
-- ORDER BY rental_count ASC
-- LIMIT 5;

-- SELECT film.title
-- FROM film
-- JOIN language ON film.language_id = language.language_id
-- WHERE language.name = 'English' AND film.release_year = 2006;




