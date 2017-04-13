from bitFont import BitFont
font = BitFont(
	height = 13,
	pixBytes = bytearray(b'\xfc\x85\x03\x00\x00\x0e\x00\n\xf0\x07(\xc0\x1f\xa0\x00$@\x05\xfc\x01\x15 \x01\x82\xa1\x08\x88\x00L@\x14\x06\x016 \t$\x01+\x00\x02\xa0p\x00p\x801\x08\x08\x01\xc1\x18\xe0\x00\x08@\x05p\x00\x0e\xa0\x02\x10\x00\x02@\x00>\x00\x01 \x00\x80\x00\x0c\x80\x01\x10@\x00\x08\x00\x01 \x00\x04\x00\x08\x80\x03 \x00\x060\x00\x01\x18\xc0\x00\xe0\x03\x82  \x04\x04A\xc0\x07\x08\x82@\xf8\x0f\x00\x01 \x18\x86\xa0\x10\x12BBDp\x08\x81  D\x84\x8cP\x11\xc6\x01\x1c@\x02D@\x08\xfc\x07 \xf0\t"BBH\x08\t!\x1e\xf0\x03\x91\x10\x11"BD\x00\x07\x01 0\x84\x81\x0cP\x00\x06\x80;\x88\x08\x11!"D\x04w\xe0\x00"BD\x88\x08\x89\xc0\x0f \x04\xce\x81\x10\x00\x04b\xe0\x0c\x88\x00\x02\xa0\x00" \x08\x02\x02\x12@\x02H\x00\t \x01$\x10\x10\x04\x01\x11@\x01\x10\xc0\x00\x04\x80\x00\x10\x16"\x80\x03\xf0\x07\x01!&$\x85\x94\xe0\x07\xf8\x83\x08\x08\x01!@\x04\xf0\x87\x80\xf0\x1f"BD\x88\x08\xee\xc0\x1f\x04\x84\x80\x10\x10\x02\x82 \x08\x08\xff! \x04\x84\x80\xe0\x0f\xfeCD\x88\x08\x11! \x04\x84\xff\x10\x01"@\x04\x08\x00\x01\xc0\x1f\x04\x84\x80\x10\x12B\x81x\xf8\x0f\x10\x00\x02@\x00\x08\xf0\x1f\x02B@\xf8\x0f\x01! \x00\x02\x80\x00\x10\x02\xc2?\x08\x00\xff\x01\x02\xa0\x00" \x08\x02\xc2\x7f\x00\x08\x00\x01 \x00\x04\x80\xf0\x1f\x0c\x00\x06\xc0\x00\x06\xe0?\xfc\x07\x02\x80\x00 \x00\x08\xf8\x0f\xfe  \x04\x84\x80\x10\x10\xfc\xc1\x7f\x88\x00\x11 \x02D\x00\x07\xe0\x0f\x02BP\x08\x0c\x01\xc1_\xfc\x87\x08\x10\x03\xa2@$p\x08\x8e "D\x84\x88\x10\x11\xc4A\x00\x08\x00\xff!\x00\x04\x80\x7f\x00\x10\x00\x02@\x00\x08\xff\xe0\x00\xe0\x00\xe0\x00\x1cp\xc0\x01\xf8\x0f\xc0\x00\x06\xc0\x00`\xf0\x1f\x06\x03\x1b\x80\x00\x10\x80\r\x0c\x86\x01\xc0\x00\xe0\x03\x03\x18\x00\x81!(\xc4\x84\x8cP\x10\x06\xe2\xff\x04\x90\x00\x12@\x0c\x00\x06\x00\x01\xc0\x00`\x04\x90\x00\x12@\xfe\x0f\x02 \x00\x02\x80\x00 \x00\x00\x02@\x00\x08\x00\x01 \x00$\x00\x08\x00\xc0\x00%\xa0\x04\x94\x80\n\xe0\xc3\x7f\x80\x04\x08\x01! \x04x\x00\x0f\x10\x02B@\x08\x08\x01\x12\xc0\x03\x84\x80\x10\x10\x02$\xf8\x0f\xf0\x00%\xa0\x04\x94\x80\x12`\x01\x04\xf0\x0f\x11 \x02\x04\x00\x01\x00+\x90\nRA*0\x05A\xfc\x07\x08\x80\x00\x10\x00\x02\x80\x0f\x00\x01!\xe8\x07\x80\x00\x10\x00\x06\x00\x01 \x08D\x7f\xfc\x07\x10\x00\x02\xa0\x00"\x00\x08\x00! \xfc\x07\x80\x00\x10\xf0\x03\x02\x80\x07\x08\x00>\xe0\x07\x08\x80\x00\x10\x00\x02\x80\x0f\xf0\x00! \x04\x84\x80\x10\xe0\x01\xfe\x81\x02\x88\x00\x11 \x028\x00\x07\x10\x01"@\x04P\x00\xff \x00\xf8\x80\x00\x10\x00\x02\x80\x00\x90\x00%\xa0\x04\xa4\x80\x14 \x01\x02\xf0\x07\x08\x01!\x00\x04@\x80\x0f\x00\x02@\x00\x08\x80\x00?\xe0\x00`\x00\x10\x80\x01\x0e\xc0\x07\x00\x01\x1c\x00\x04|\x80\x10 \x01\x18\x00\x03\x90\x00!\xe0\t@\x02H\x00\t\x10\xc1\x1f\x08\x011 \x05\x94\x80\x11\x10\x02\x04\xb8\x8e(\x12@\x02\x88\xff\x08 \x01$\x8a\xb8\x0e\x10\xc0\x00\x04\x00\x01@\x00\x06'),
	endCols = [1, 4, 9, 14, 20, 26, 27, 30, 33, 39, 44, 48, 53, 56, 61, 67, 72, 78, 84, 90, 96, 102, 108, 114, 120, 123, 127, 132, 138, 143, 149, 155, 161, 167, 173, 179, 185, 191, 197, 203, 208, 214, 220, 226, 232, 238, 244, 250, 256, 262, 268, 273, 279, 285, 291, 297, 302, 308, 312, 317, 321, 326, 332, 334, 340, 346, 352, 358, 364, 370, 376, 382, 387, 392, 398, 403, 408, 414, 420, 426, 432, 438, 444, 450, 456, 461, 466, 472, 478, 484, 489, 490, 495, 500]
)