INSERT INTO Users (username, password, email) 
VALUES 
		('admin', 'admin', 'admin@example.com'),
		('adalovelace', 'adalovelace', 'adalovelace@example.com'),
		('user2', 'user2', 'user2@example.com');
		
INSERT INTO Events (event_name, event_date, event_description, event_location, user_id)
VALUES
		('Friendsgiving', '2023-12-09 15:00:00', 'A Thanksgiving for friends!', '2800 Waterview Pkwy', 1);
		
INSERT INTO RSVPs (user_id, event_id)
VALUES
		(1, 1),
		(2, 1),
		(3, 1);
		
INSERT INTO Food (event_id, rsvp_id, food_name, servings)
VALUES
		(1, 1, 'Turkey', 10),
		(1, 1, 'Mashed Potatoes', 5),
		(1, 1, 'Gravy', 5),
		(1, 1, 'Stuffing', 8),
		(1, 2, 'Green Beans', 12),
		(1, 2, 'Cranberry Sauce', 15),
		(1, 2, 'Pumpkin Pie', 2),
		(1, 2, 'Apple Pie', 2),
		(1, 2, 'Ice Cream', 5);