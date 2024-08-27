# Draw4ORCA

- **A range of ORCA drawing kits for personal use**，The legend is in each corresponding file package
- **constantly updated**

# How to Use
## 4ofakeg
```bash
python draw_4ofakeg.py 1_fake.out  2_fake.out  etc...
*OR*
python draw_4ofakeg.py  *_fake.out 
```
- Based on matplotlib and Ofakeg produced by *Lu Tian*, ​​it can accept one or more ```*_fake.out files```. And draw SCF energy changes, maximum force changes, etc.
- Applicable to general **sp** or **opt** Gaussian output files, but the energy change diagram will not be drawn.

## scan
```bash
python draw_scan.py ScanTS.relaxscanact.dat relative
*OR*
python draw_4ofakeg.py  ScanTS.relaxscanact.dat  [NOW it is absolute]
```
- Using ORCA for flexible scanning will eventually give ```ScanTS.relaxscanact.dat```, and you can draw by executing this script.
