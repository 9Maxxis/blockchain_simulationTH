# (BlockchainTH) Blockchain Simulation by 9Maxxis

PyPI: https://pypi.org/project/blockchain_simulationTH/

โปรแกรมนี้เป็นโปรแกรมภาษาไพทอนที่ใช้สำหรับจำลองการทำงานของเครือข่ายบล็อกเชนอย่างง่ายเพื่อเป็นแหล่งเรียนรู้สำหรับบุคคลทั่วไปที่มีความสนใจในเทคโนโลยีบล็อกเชนให้สามารถศึกษาการจำลองการทำงานของเครือข่ายบล็อกเชนที่ผู้จัดทำได้สร้างขึ้น  เพื่อประกอบความรู้และความเข้าใจในเทคโนโลยีบล็อกเชน 

ปล1. ต้องดาวโหลด Python ก่อนจาก https://www.python.org/
ปล2. ผู้จัดทำยังมือใหม่ หากผิดพลาดประการใด ทำขออภัยมา ณ ที่นี้ด้วยนะจ๊ะ
ปล3. ขอบคุณวิธีสร้าง Python packet เป็นของตัวเองและวิธีอัพโหลด Packet ไปยัง PyPI.org จาก https://www.youtube.com/watch?v=1egtTXUJ3-4

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install blockchain_simulationTH
```

### วิธีใช้

[STEP 1]เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
import blockchain_simulationTH
```

[STEP 2] สร้างผู้ใช้
```python
    ชื่อตัวแปร(เป็นอะไรก็ได้)   =  Client('ชื่อของผู้ใช้')
```
-เช่น
```python  
     #Client A
     A = Client('A')

      #Client B
      B = Client('B')
    
      #Client C
      C = Client('C')
```

[STEP 3] สร้าง Coinbase Transaction สำหรับเป็นเงินตั้งต้นให้แก่ผู้ใช้แต่ละคน
```python
ชื่อตัวแปร(เป็นอะไรก็ได้) = Coinbase(ชื่อธุรกรรม(เป็นอไรก็ได้) ,ชื่อตัวแปรผู้ใช้ในขั้นตอนที่ 1 ,ปริมาณเงินที่ต้องการ)
```
-เช่น
```python
      coinbasetx1 = Coinbase('coin1',A,1000)
      coinbasetx2 = Coinbase('coin2',B,1000)
      coinbasetx3 = Coinbase('coin3',C,1000)
```

[STEP 4] สร้าง Block แรกของระบบ
```python
ชื่อตัวแปร(เป็นอะไรก็ได้)  = Genesisblock(ชื่อ Coinbase Transaction ในขั้นตอนที่แล้ว)
```
-เช่น
```python
        block = Genesisblock('coin1','coin2','coin3')
```

[STEP 5} กระบวนการ Proof of work
```python
ชื่อตัวแปร(เป็นอะไรก็ได้)  = mine(ชื่อบล็อกในขั้นตอนที่แล้ว,prefix zero)
```
-prefix zero คือ จำนวนบิตเลขศูนย์เริ่มต้นของ block hash ซึ่งเป็นผลลัพธ์ของกระบวนการ Proof of work -โดยเป็น prefix zero เป็นการกำหนดค่าเป้าหมาย (Target) ในกระบวนการ Proof of work ดังสมการ

                                   Target = 2**(256-Prefix zero)   
-เช่น
```python
POW = mine(block,3)
```
[STEP 6] สร้างธุรกรรม
```python
ชื่อตัวแปร(เป็นอะไรก็ได้) = Transaction(ชื่อธุรกรรม(เป็นอะไรก็ได้),ชื่อของผู้ใช้ที่ต้องการให้เป็นผู้ส่ง, ชื่อของผู้ใช้ที่ต้องการให้เป็นผู้รับ,ปริมาณเงินที่ผู้ส่งจะโอนไปยังผู้รับ, ชื่อของธุรกรรมที่อ้างอิงถึง,ลำดับของเอาต์พุตของธุรกรรมที่ผู้ส่งอ้างอิงถึงนั้น) 
```
ปล. สำหรับ Coinbase Transaction มีลำดับเอาต์พุตของธุรกรรมแค่ลำดับเดียว คือ index = 0 แต่ Transaction ทั่วไปมีลำดับเอาต์พุตของธุรกรรม 2 ลำดับ ดังนี้ index = 0 คือ ส่งกลับให้ตัวเอง และ index = 1 คือ ส่งให้ผู้อื่น

-เช่น
```python
        tx1 = Transaction('tx1',A,B,50,'coin1',0)
        tx2 = Transaction('tx2',B,C,100,'coin2',0)
        tx3 = Transaction('tx3',C,A,70,'coin3',0)
```
[STEP 7] สร้างบล็อก
```python
ชื่อตัวแปร(เป็นอะไรก็ได้)  = Block(ชื่อธุรกรรมในขั้นตอนที่แล้ว)
```
-เช่น
```python
block1 = Block('tx1','tx2','tx3')
```
[STEP 8] กระบวนการ Proof of work
```python
ชื่อตัวแปร(เป็นอะไรก็ได้)  = mine(ชื่อบล็อกในขั้นตอนที่แล้ว,prefix zero)
```
-เช่น
```python
POW = mine(block1,5) 
```
[STEP 9] ตรวจสอบเงินในบัญชีของผู้ใช้แต่ละคน
```python
print(ชื่อตัวแปรของผู้ใช้ในขั้นตอนที่ 1.view_balance())
```
```python
        print(A.view_balance())
        print(B.view_balance())
        print(C.view_balance()) 
```
[STEP 10] ทำซ้ำขั้นตอนที่ 6-8 ไปเรื่อย ๆ จนกว่าท่านจะพอใจ

พัฒนาโดย: 9Maxxis