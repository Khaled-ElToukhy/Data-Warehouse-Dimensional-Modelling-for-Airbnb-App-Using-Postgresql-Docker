
calender_table_insert = ("""
                            INSERT INTO calender
                                (list_id,
                                date,
                                available,
                                price)
                            VALUES
                                (%s, %s, %s, %s)
""")


reviews_table_insert = ("""
                            INSERT INTO reviews
                                (list_id,
                                date)
                            VALUES
                                (%s, %s)
""")



listings_table_insert = ("""
                            INSERT INTO listings
                            (id,
                            name, 
                            host_id,
                            host_name,
                            neighbourhood,
                            latitude,
                            longitude,
                            room_type,
                            price,
                            min_height)
                            VALUES
                                (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)
""")


reviews_details_table_insert = ("""
                            INSERT INTO reviewsDetails
                                (list_id,
                                id,
                                date,
                                reviewer_id,
                                reviewer_name,
                                comments
                                )
                            VALUES
                                (%s, %s, %s, %s, %s, %s)
""")