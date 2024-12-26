pip install tkcalendar
Kịch bản Chạy
1. Màn hình chính (Main.py)
Khi chương trình được chạy, cửa sổ chính sẽ mở ra với giao diện quản lý sự kiện.

Giao diện chính bao gồm các nút sau:

Book Tickets: Đặt vé
Create Event: Tạo sự kiện mới
View Ticket: Xem các vé đã đặt
View Events: Xem các sự kiện đã tạo
Cancel Ticket: Hủy vé đã đặt
Quit: Thoát ứng dụng
Các nút này sẽ dẫn người dùng đến các chức năng tương ứng. Khi người dùng nhấn vào một nút, cửa sổ hiện tại sẽ bị đóng và chuyển sang cửa sổ mới để thực hiện chức năng yêu cầu.

2. Khi người dùng nhấn "Book Tickets"
Quá trình:
Khi người dùng nhấn nút "Book Tickets", cửa sổ chính sẽ bị đóng.
Hàm Book() trong file Book.py sẽ được gọi, mở cửa sổ mới để người dùng thực hiện thao tác đặt vé.
Giao diện cửa sổ "Book Tickets":
Cửa sổ hiện thị dòng chữ "Chức năng đặt vé".
Có một nút "Back" để quay lại màn hình chính.
3. Khi người dùng nhấn "Create Event"
Quá trình:
Khi người dùng nhấn nút "Create Event", cửa sổ chính sẽ bị đóng.
Hàm CreateEvent() trong file CreateEvent.py sẽ được gọi, mở cửa sổ mới để người dùng tạo sự kiện.
Giao diện cửa sổ "Create Event":
Cửa sổ hiện thị dòng chữ "Chức năng tạo sự kiện".
Có một nút "Back" để quay lại màn hình chính.
4. Khi người dùng nhấn "View Ticket"
Quá trình:
Khi người dùng nhấn nút "View Ticket", cửa sổ chính sẽ bị đóng.
Hàm ViewTickets() trong file ViewTickets.py sẽ được gọi, mở cửa sổ mới để người dùng xem các vé đã đặt.
Giao diện cửa sổ "View Ticket":
Cửa sổ hiện thị dòng chữ "Danh sách vé đã đặt".
Có một nút "Back" để quay lại màn hình chính.
5. Khi người dùng nhấn "View Events"
Quá trình:
Khi người dùng nhấn nút "View Events", cửa sổ chính sẽ bị đóng.
Hàm ViewEvents() trong file ViewEvents.py sẽ được gọi, mở cửa sổ mới để người dùng xem các sự kiện đã tạo.
Giao diện cửa sổ "View Events":
Cửa sổ hiện thị dòng chữ "Danh sách sự kiện".
Có một nút "Back" để quay lại màn hình chính.
6. Khi người dùng nhấn "Cancel Ticket"
Quá trình:
Khi người dùng nhấn nút "Cancel Ticket", cửa sổ chính sẽ bị đóng.
Hàm CancelTicket() trong file CancelTicket.py sẽ được gọi, mở cửa sổ mới để người dùng hủy vé đã đặt.
Giao diện cửa sổ "Cancel Ticket":
Cửa sổ hiện thị dòng chữ "Chức năng hủy vé".
Có một nút "Back" để quay lại màn hình chính.
7. Khi người dùng nhấn "Quit"
Quá trình:
Khi người dùng nhấn nút "Quit", cửa sổ chính sẽ bị đóng.
Chương trình sẽ kết thúc và ứng dụng sẽ thoát.
Lưu đồ và Mô tả
1. Khởi động ứng dụng (Main.py)

css
Copy code
+-------------------------------------+
|             Màn hình chính          |
|-------------------------------------|
| [Book Tickets] [Create Event]       |
| [View Ticket]   [View Events]       |
| [Cancel Ticket] [Quit]              |
+-------------------------------------+
2. Nếu người dùng nhấn "Book Tickets"

css
Copy code
Cửa sổ chính đóng → Cửa sổ Book Tickets mở → [Back] → Trở lại cửa sổ chính
3. Nếu người dùng nhấn "Create Event"

css
Copy code
Cửa sổ chính đóng → Cửa sổ Create Event mở → [Back] → Trở lại cửa sổ chính
4. Nếu người dùng nhấn "View Ticket"

css
Copy code
Cửa sổ chính đóng → Cửa sổ View Ticket mở → [Back] → Trở lại cửa sổ chính
5. Nếu người dùng nhấn "View Events"

css
Copy code
Cửa sổ chính đóng → Cửa sổ View Events mở → [Back] → Trở lại cửa sổ chính
6. Nếu người dùng nhấn "Cancel Ticket"

css
Copy code
Cửa sổ chính đóng → Cửa sổ Cancel Ticket mở → [Back] → Trở lại cửa sổ chính
7. Nếu người dùng nhấn "Quit"

css
Copy code
Cửa sổ chính đóng → Ứng dụng kết thúc
Tổng kết
Khi chương trình được chạy, người dùng sẽ thấy một giao diện chính với các nút để tương tác với các chức năng khác nhau của ứng dụng quản lý sự kiện. Mỗi chức năng (đặt vé, tạo sự kiện, xem vé, xem sự kiện, hủy vé) sẽ mở một cửa sổ riêng biệt. Người dùng có thể quay lại màn hình chính bất cứ lúc nào bằng cách nhấn nút "Back", và có thể thoát ứng dụng bằng nút "Quit".

Các cửa sổ con được xây dựng bằng các module riêng biệt (Book.py, CreateEvent.py, ViewTickets.py, ViewEvents.py, CancelTicket.py) sẽ được mở khi người dùng nhấn các nút tương ứng từ giao diện chính.
