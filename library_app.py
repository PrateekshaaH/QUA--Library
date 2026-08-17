import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt


# Database Connection
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",  # Adjust as needed
            database="library_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
        return None


# Main Page
def main_page():
    # Define colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create main window
    main_window = tk.Tk()
    main_window.title("Welcome to QUA Library")
    main_window.geometry("500x400")
    main_window.configure(bg=c)

    # Add widgets
    tk.Label(
        main_window,
        text="QUA LIBRARY",
        font=("Times New Roman", 30, "italic bold"),
        bg=c,
        fg=m
    ).pack(pady=50)

    tk.Button(
        main_window,
        text="Login",
        command=login_page,
        font=("Arial", 16),
        bg=m,
        fg="white",
        activebackground=m,
        activeforeground=c
    ).pack(pady=20)

    main_window.mainloop()


# Login Page
def login_page():
    # Define colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    login_window = tk.Toplevel()
    login_window.title("Admin Login")
    login_window.geometry("300x200")
    login_window.configure(bg=c)

    tk.Label(
        login_window,
        text="Username",
        font=("Arial", 12),
        bg=c,
        fg=m
    ).pack(pady=5)

    entry_username = tk.Entry(login_window, font=("Arial", 12))
    entry_username.pack(pady=5)

    tk.Label(
        login_window,
        text="Password",
        font=("Arial", 12),
        bg=c,
        fg=m
    ).pack(pady=5)

    entry_password = tk.Entry(login_window, show="*", font=("Arial", 12))
    entry_password.pack(pady=5)

    def check_credentials():
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "admin123":
            login_window.destroy()
            admin_or_graph_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    tk.Button(
        login_window,
        text="Login",
        command=check_credentials,
        font=("Arial", 12),
        bg=m,
        fg="white",
        activebackground=m,
        activeforeground=c
    ).pack(pady=10)


# Admin or Graph Menu
def admin_or_graph_menu():
    # Define colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    options_window = tk.Toplevel()
    options_window.title("Options")
    options_window.geometry("300x200")
    options_window.configure(bg=c)

    # Create a frame to center the buttons
    frame = tk.Frame(options_window, bg=c)
    frame.pack(expand=True)

    tk.Button(
        frame,
        text="Admin",
        command=open_admin_options,
        font=("Arial", 12),
        bg=m,
        fg="white",
        activebackground=m,
        activeforeground=c
    ).pack(pady=10)

    tk.Button(
        frame,
        text="Graphs",
        command=show_graphs_menu,
        font=("Arial", 12),
        bg=m,
        fg="white",
        activebackground=m,
        activeforeground=c
    ).pack(pady=10)


# Admin Options
def open_admin_options():
    # Define color variables
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window
    admin_window = tk.Toplevel()
    admin_window.title("Admin Options")
    admin_window.geometry("300x400")

    # Set the background color for the admin window
    admin_window.configure(bg=c)

    # Create buttons with the specified theme colors
    tk.Button(admin_window, text="Book Issue",
              command=book_issue_window, bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="Book Return",
              command=book_return_window, bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="Add Book", command=add_book, bg=m,
              fg="white").pack(pady=5)
    tk.Button(admin_window, text="Search Book", command=search_book,
              bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="View All Books",
              command=view_all_books, bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="Delete Book", command=delete_book,
              bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="Membership List",
              command=view_membership_list, bg=m, fg="white").pack(pady=5)
    tk.Button(admin_window, text="Book Record",
              command=view_book_record, bg=m, fg="white").pack(pady=5)


def add_book():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for adding a book
    add_book_window = tk.Toplevel()
    add_book_window.title("Add Book")
    add_book_window.geometry("300x400")
    add_book_window.configure(bg=c)  # Set the background color of the window

    # Book ID
    tk.Label(add_book_window, text="Book ID", bg=c, fg=m).pack()
    entry_id = tk.Entry(add_book_window)
    entry_id.pack()

    # Book Name
    tk.Label(add_book_window, text="Book Name", bg=c, fg=m).pack()
    entry_name = tk.Entry(add_book_window)
    entry_name.pack()

    # Author
    tk.Label(add_book_window, text="Author", bg=c, fg=m).pack()
    entry_author = tk.Entry(add_book_window)
    entry_author.pack()

    # Genre
    tk.Label(add_book_window, text="Genre", bg=c, fg=m).pack()
    entry_genre = tk.Entry(add_book_window)
    entry_genre.pack()

    # Quantity
    tk.Label(add_book_window, text="Quantity", bg=c, fg=m).pack()
    entry_quantity = tk.Entry(add_book_window)
    entry_quantity.pack()

    # Publication Date
    tk.Label(add_book_window, text="Publication Date (YYYY-MM-DD)",
             bg=c, fg=m).pack()
    entry_pub_date = tk.Entry(add_book_window)
    entry_pub_date.pack()

    # Publisher Name
    tk.Label(add_book_window, text="Publisher Name", bg=c, fg=m).pack()
    entry_publisher = tk.Entry(add_book_window)
    entry_publisher.pack()

    def save_and_close():
        book_id = entry_id.get()
        name = entry_name.get()
        author = entry_author.get()
        genre = entry_genre.get()
        quantity = entry_quantity.get()
        pub_date = entry_pub_date.get()
        publisher = entry_publisher.get()

        # Connect to the database
        conn = connect_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books (book_id, book_name, author, genre,
                quantity, publication_date, publisher_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (book_id, name, author, genre, quantity, pub_date, publisher))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully.")
            add_book_window.destroy()  # Close the window only on success
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add book: {err}")
        finally:
            cursor.close()
            conn.close()

    # Button to save and close
    tk.Button(add_book_window, text="Add Book",
              command=save_and_close, bg=m, fg='white').pack(pady=10)


def search_book():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for search
    search_window = tk.Toplevel()
    search_window.title("Search Book")
    search_window.geometry("400x300")
    search_window.configure(bg=c)  # Set the background color of the window

    # Label for entering Book ID or Name
    tk.Label(search_window, text="Enter Book ID or Name", bg=c,
             fg=m).pack(pady=10)
    entry_search = tk.Entry(search_window)
    entry_search.pack(pady=5)

    def display_search_result():
        query = entry_search.get()
        conn = connect_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE book_id = %s OR "
                            "book_name LIKE %s",
                            (query, '%' + query + '%'))
            result = cursor.fetchall()

            if not result:
                messagebox.showinfo("No Results", "No books found matching the query.")
                return

            search_window.destroy()  # Close the search window

            # Create a new window to display results
            result_window = tk.Toplevel()
            result_window.title("Search Results")
            result_window.geometry("600x400")
            result_window.configure(bg=c)

            columns = ["book_id", "book_name", "author", "genre", "quantity",
                       "publication_date", "publisher_name"]
            treeview = ttk.Treeview(result_window, columns=columns,
                                     show="headings")

            for col in columns:
                treeview.heading(col, text=col)
                treeview.column(col, width=150, anchor="center")

            for row in result:
                treeview.insert("", "end", values=row)

            treeview.pack(fill="both", expand=True)

            def close_results():
                result_window.destroy()

            tk.Button(result_window, text="Close", command=close_results,
                      bg=m, fg='white').pack(pady=10)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Search failed: {err}")
        finally:
            cursor.close()
            conn.close()

    # Button to start search
    tk.Button(search_window, text="Search",
              command=display_search_result, bg=m, fg='white').pack(pady=10)


def view_all_books():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for viewing all books
    view_window = tk.Toplevel()
    view_window.title("All Books")
    view_window.geometry("600x400")
    view_window.configure(bg=c)  # Set the background color

    # Connect to the database
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()

        # Define columns for the Treeview
        columns = ["book_id", "book_name", "author", "genre", "quantity",
                   "publication_date", "publisher_name"]
        treeview = ttk.Treeview(view_window, columns=columns,
                                 show="headings")

        # Configure Treeview headings and columns
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=150, anchor="center")

        # Insert fetched data into the Treeview
        for row in result:
            treeview.insert("", "end", values=row)

        treeview.pack(fill="both", expand=True)

        # Add a Close button with the theme
        tk.Button(view_window, text="Close",
                  command=view_window.destroy, bg=m, fg='white').pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to fetch books: {err}")
    finally:
        cursor.close()
        conn.close()


def delete_book():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for deleting a book
    delete_window = tk.Toplevel()
    delete_window.title("Delete Book")
    delete_window.geometry("300x200")
    delete_window.configure(bg=c)  # Set the background color

    # Label for entering Book ID to delete
    tk.Label(delete_window, text="Enter Book ID to Delete", bg=c,
             fg=m).pack(pady=10)
    entry_delete = tk.Entry(delete_window)
    entry_delete.pack(pady=5)

    def confirm_delete():
        book_id = entry_delete.get()
        conn = connect_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE book_id = %s",
                            (book_id,))
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Book deleted successfully.")
                delete_window.destroy()  # Close the window on success
            else:
                messagebox.showwarning("Warning", "No book found with the given ID.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to delete book: {err}")
        finally:
            cursor.close()
            conn.close()

    # Button to confirm deletion
    tk.Button(delete_window, text="Delete", command=confirm_delete,
              bg=m, fg='white').pack(pady=10)


def view_membership_list():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for viewing the membership list
    view_window = tk.Toplevel()
    view_window.title("Membership List")
    view_window.geometry("600x400")
    view_window.configure(bg=c)  # Set the background color

    # Connect to the database
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        result = cursor.fetchall()

        # Define columns for the Treeview
        columns = ["member_id", "name", "email", "membership_expiration",
                   "membership_joined", "membership_pack"]
        treeview = ttk.Treeview(view_window, columns=columns,
                                 show="headings")

        # Configure Treeview headings and columns
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=150, anchor="center")

        # Insert fetched data into the Treeview
        for row in result:
            treeview.insert("", "end", values=row)

        treeview.pack(fill="both", expand=True)

        # Add a Close button with the theme
        tk.Button(view_window, text="Close",
                  command=view_window.destroy, bg=m, fg='white').pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to fetch membership list: {err}")
    finally:
        cursor.close()
        conn.close()


def view_book_record():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create a new top-level window for viewing book records
    view_window = tk.Toplevel()
    view_window.title("Book Record")
    view_window.geometry("600x400")
    view_window.configure(bg=c)  # Set the background color

    # Connect to the database
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book_records")
        result = cursor.fetchall()

        # Define columns for the Treeview
        columns = ["record_id", "book_id", "member_id", "borrow_date",
                   "return_date", "due_date"]
        treeview = ttk.Treeview(view_window, columns=columns,
                                 show="headings")

        # Configure Treeview headings and columns
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=150, anchor="center")

        # Insert fetched data into the Treeview
        for row in result:
            treeview.insert("", "end", values=row)

        treeview.pack(fill="both", expand=True)

        # Add a Close button with the theme
        tk.Button(view_window, text="Close",
                  command=view_window.destroy, bg=m, fg='white').pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to fetch book records: {err}")
    finally:
        cursor.close()
        conn.close()


# Book Issue Window
def book_issue_window():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create the issue window
    issue_window = tk.Toplevel()
    issue_window.title("Book Issue")
    issue_window.geometry("400x400")
    issue_window.configure(bg=c)  # Set background color

    # Labels and entry fields for book issue form
    tk.Label(issue_window, text="Record ID", bg=c, fg=m).pack(pady=5)
    entry_record_id = tk.Entry(issue_window)
    entry_record_id.pack()

    tk.Label(issue_window, text="Book ID", bg=c, fg=m).pack(pady=5)
    entry_book_id = tk.Entry(issue_window)
    entry_book_id.pack()

    tk.Label(issue_window, text="Member ID", bg=c, fg=m).pack(pady=5)
    entry_member_id = tk.Entry(issue_window)
    entry_member_id.pack()

    tk.Label(issue_window, text="Borrow Date (YYYY-MM-DD)", bg=c,
             fg=m).pack(pady=5)
    entry_borrow_date = tk.Entry(issue_window)
    entry_borrow_date.pack()

    tk.Label(issue_window, text="Due Date (YYYY-MM-DD)", bg=c,
             fg=m).pack(pady=5)
    entry_due_date = tk.Entry(issue_window)
    entry_due_date.pack()

    # Function to handle form submission
    def submit_issue():
        record_id = entry_record_id.get()
        book_id = entry_book_id.get()
        member_id = entry_member_id.get()
        borrow_date = entry_borrow_date.get()
        due_date = entry_due_date.get()

        conn = connect_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO book_records (record_id, book_id, member_id, "
                "borrow_date, due_date, return_date) "
                "VALUES (%s, %s, %s, %s, %s, NULL)",
                (record_id, book_id, member_id, borrow_date, due_date)
            )
            conn.commit()
            messagebox.showinfo("Success", "Book issued successfully.")
            issue_window.destroy()  # Close the window on success
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to issue book: {err}")
        finally:
            cursor.close()
            conn.close()

    # Submit button with theme
    tk.Button(issue_window, text="Submit", command=submit_issue, bg=m,
              fg='white').pack(pady=10)


# Book Return Window
def book_return_window():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create the return window
    return_window = tk.Toplevel()
    return_window.title("Book Return")
    return_window.geometry("600x400")
    return_window.configure(bg=c)  # Set background color

    # Open a connection for fetching data
    conn_fetch = connect_db()
    if conn_fetch is None:
        return

    try:
        cursor_fetch = conn_fetch.cursor()
        cursor_fetch.execute("SELECT * FROM book_records WHERE return_date IS NULL")
        rows = cursor_fetch.fetchall()

        # Define columns for the Treeview
        columns = ["record_id", "book_id", "member_id", "borrow_date", "due_date"]
        treeview = ttk.Treeview(return_window, columns=columns,
                                 show="headings")

        # Configure Treeview headings and columns
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=100, anchor="center")

        for row in rows:
            treeview.insert("", "end", values=row)

        treeview.pack(fill="both", expand=True)

        # Function to update the return date
        def update_return_date():
            selected_item = treeview.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "No item selected.")
                return

            record_id = treeview.item(selected_item[0])['values'][0]

            # Function to submit the return date
            def submit_return_date():
                return_date = entry_return_date.get()
                if not return_date:
                    messagebox.showerror("Error", "Please enter a return date.")
                    return

                # Open a new connection for the update
                conn_update = connect_db()
                if conn_update is None:
                    return

                try:
                    cursor_update = conn_update.cursor()
                    cursor_update.execute(
                        "UPDATE book_records SET return_date = %s WHERE record_id = %s",
                        (return_date, record_id)
                    )
                    conn_update.commit()
                    messagebox.showinfo("Success", "Book return date updated.")
                    treeview.delete(selected_item)
                    return_date_window.destroy()
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to update return date: {err}")
                finally:
                    cursor_update.close()
                    conn_update.close()

            # Create a new window for entering the return date
            return_date_window = tk.Toplevel(return_window)
            return_date_window.title("Enter Return Date")
            return_date_window.geometry("300x200")
            return_date_window.configure(bg=c)

            tk.Label(return_date_window, text="Return Date (YYYY-MM-DD)",
                     bg=c, fg=m).pack(pady=5)
            entry_return_date = tk.Entry(return_date_window)
            entry_return_date.pack(pady=5)

            tk.Button(return_date_window, text="Submit",
                      command=submit_return_date, bg=m, fg='white').pack(pady=10)

        # Add buttons with the theme
        tk.Button(return_window, text="Mark as Returned",
                  command=update_return_date, bg=m, fg='white').pack(pady=10)
        tk.Button(return_window, text="Close",
                  command=return_window.destroy, bg=m, fg='white').pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to fetch records: {err}")
    finally:
        cursor_fetch.close()
        conn_fetch.close()


# Graphs Menu
def show_graphs_menu():
    # Define theme colors
    c = "#BDD3CE"  # Background color
    m = "#013D5A"  # Font color

    # Create the graph window
    graph_window = tk.Toplevel()
    graph_window.title("Graphs Menu")
    graph_window.geometry("300x200")
    graph_window.configure(bg=c)  # Set background color

    # Make graph_window transient and modal to avoid affecting other windows
    graph_window.transient()  # Makes it always appear above its parent window
    graph_window.grab_set()  # Blocks interaction with other windows until closed

    # Add buttons with the theme
    tk.Button(graph_window, text="Top Borrowed Books",
              command=graph_top_borrowed_books, bg=m, fg='white').pack(pady=10)
    tk.Button(graph_window, text="Books by Genre",
              command=graph_books_by_genre, bg=m, fg='white').pack(pady=10)
    tk.Button(graph_window, text="Monthly Borrowing Trend",
              command=graph_monthly_borrowing_trend, bg=m,
              fg='white').pack(pady=10)
    tk.Button(graph_window, text="Membership Distribution",
              command=graph_membership_distribution, bg=m,
              fg='white').pack(pady=10)

    # Prevent resizing of the graph window
    graph_window.resizable(False, False)


# Graph Functions
def graph_top_borrowed_books():
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT b.book_name, COUNT(*) AS borrow_count
            FROM book_records br
            JOIN books b ON br.book_id = b.book_id
            GROUP BY b.book_id
            ORDER BY borrow_count DESC
            LIMIT 5
            """
        )
        data = cursor.fetchall()

        book_names = [row['book_name'] for row in data]
        borrow_counts = [row['borrow_count'] for row in data]

        plt.bar(book_names, borrow_counts, color='blue')
        plt.title("Top 5 Most Borrowed Books")
        plt.xlabel("Books")
        plt.ylabel("Borrows")
        plt.xticks(rotation=45)
        plt.show()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to generate graph: {err}")
    finally:
        cursor.close()
        conn.close()


def graph_books_by_genre():
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT genre, COUNT(*) AS book_count
            FROM books
            GROUP BY genre
            ORDER BY book_count DESC
            """
        )
        data = cursor.fetchall()

        genres = [row['genre'] for row in data]
        counts = [row['book_count'] for row in data]

        plt.pie(counts, labels=genres, autopct='%1.1f%%', startangle=140)
        plt.title("Books by Genre")
        plt.show()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to generate graph: {err}")
    finally:
        cursor.close()
        conn.close()


def graph_monthly_borrowing_trend():
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT DATE_FORMAT(borrow_date, '%Y-%m') AS month,
            COUNT(*) AS borrow_count
            FROM book_records
            GROUP BY month
            ORDER BY month
            """
        )
        data = cursor.fetchall()

        months = [row['month'] for row in data]
        borrow_counts = [row['borrow_count'] for row in data]

        plt.plot(months, borrow_counts, marker='o', linestyle='-', color='green')
        plt.title("Monthly Borrowing Trend")
        plt.xlabel("Month")
        plt.ylabel("Number of Borrows")
        plt.xticks(rotation=45)
        plt.show()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to generate graph: {err}")
    finally:
        cursor.close()
        conn.close()


def graph_membership_distribution():
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT m.membership_pack, COUNT(*) AS member_count
            FROM members m
            GROUP BY m.membership_pack
            """
        )
        data = cursor.fetchall()

        packs = [row['membership_pack'] for row in data]
        counts = [row['member_count'] for row in data]

        plt.bar(packs, counts, color='orange')
        plt.title("Membership Distribution")
        plt.xlabel("Membership Pack")
        plt.ylabel("Number of Members")
        plt.xticks(rotation=45)
        plt.show()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to generate graph: {err}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main_page()
