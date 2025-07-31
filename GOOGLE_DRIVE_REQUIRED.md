# Hướng dẫn bắt buộc: Thiết lập Google Drive cho download

## ⚠️ QUAN TRỌNG: Bắt buộc phải cấu hình Google Drive

Ứng dụng này **CHỈ** sử dụng Google Drive để tải file. Bạn PHẢI thiết lập Google Drive URL trước khi chạy ứng dụng.

## Bước 1: Upload file lên Google Drive

1. Truy cập [Google Drive](https://drive.google.com)
2. Upload file `Mahika.exe` (hoặc file ứng dụng của bạn)
3. Right-click vào file → "Get link"
4. Chọn "Anyone with the link" có thể xem
5. Copy link

## Bước 2: Chuyển đổi Google Drive link thành direct download link

**Link gốc từ Google Drive:**

```
https://drive.google.com/file/d/1ABC123DEF456XYZ/view?usp=sharing
```

**Chuyển thành direct download link:**

```
https://drive.google.com/uc?export=download&id=1ABC123DEF456XYZ
```

Chỉ cần thay `1ABC123DEF456XYZ` bằng FILE_ID thực tế của bạn.

## Bước 3: Cập nhật .env

```properties
DOWNLOAD_FILE_URL=https://drive.google.com/uc?export=download&id=YOUR_REAL_FILE_ID
DOWNLOAD_FILE_NAME=Mahika.exe
```

## Bước 4: Test local

1. Restart Flask app
2. Login → Dashboard → Download
3. File sẽ được tải trực tiếp từ Google Drive

## ✅ Lợi ích của Google Drive

- **Không tốn dung lượng deploy** - File không cần upload lên server
- **Download nhanh, ổn định** - Google Drive có bandwidth cao
- **Dễ cập nhật file** - Chỉ cần thay file trên Drive, không cần redeploy
- **Miễn phí** - Không mất phí cho bandwidth
- **Bảo mật** - File chỉ tải được sau khi user đã thanh toán và verify email

## 🚨 Lưu ý quan trọng

- File PHẢI được set là public ("Anyone with the link can view")
- PHẢI sử dụng direct download link format (`uc?export=download&id=`)
- Test link trước khi deploy để đảm bảo hoạt động
- Nếu không cấu hình `DOWNLOAD_FILE_URL`, ứng dụng sẽ báo lỗi

## 🔧 Troubleshooting

**Nếu download không hoạt động:**

1. Kiểm tra file có public không
2. Kiểm tra link có đúng format không
3. Kiểm tra file ID có chính xác không
4. Test link bằng cách mở trực tiếp trong browser

**Nếu muốn thay đổi file:**

1. Upload file mới lên Google Drive
2. Cập nhật `DOWNLOAD_FILE_URL` với file ID mới
3. Restart ứng dụng
