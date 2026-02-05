# Suggested Build: Home Server (Frigate + Docker)

Generated: 2026-02-05
Catalog: 2026-02-05_13-52-27
Based on: builds/1/task.md

## Summary

This build replaces the failed motherboard with a compact, efficient home server platform optimized for Docker workloads and Frigate NVR with 3 cameras. Key design choices:

- **Intel i5-14400** selected for its 10 cores (6P+4E) and integrated UHD 730 GPU for Frigate hardware Quick Sync transcoding
- **DDR4 motherboard** to reuse existing RAM
- **Micro-ATX form factor** for compact case options while maintaining good expandability
- **PCIe 2.5G network card** to meet your 2.5G Ethernet requirement (unless your existing TP-Link card is 2.5G)

## Components

| Component | Product | Price (ILS) | Link |
|-----------|---------|-------------|------|
| CPU | Intel Core i5-14400 (Raptor Lake Tray) | ₪995 | [Link](https://www.ivory.co.il/catalog.php?id=85515) |
| Motherboard | Gigabyte B760M DS3H DDR4 (mATX) | ₪439 | [Link](https://www.ivory.co.il/catalog.php?id=62097) |
| CPU Cooler | Arctic Alpine 17 CO 1700/1851 | ₪55 | [Link](https://www.ivory.co.il/catalog.php?id=70385) |
| Case | Jonsbo C6 White (Micro-ATX) | ₪265 | [Link](https://www.ivory.co.il/catalog.php?id=95028) |
| Network Card | Cudy PE25 2.5Gbps PCIe | ₪79 | [Link](https://www.ivory.co.il/catalog.php?id=57950) |

**Total (New Components): ₪1,833**

## Compatibility Notes

- **CPU ↔ Motherboard**: ✅ Intel i3-14100 (LGA1700) is compatible with B760 chipset
- **RAM ↔ Motherboard**: ✅ B760M DS3H supports DDR4 (matches your salvaged RAM)
- **Case ↔ Motherboard**: ✅ Jonsbo C6 supports Micro-ATX
- **Case ↔ PSU**: ✅ Jonsbo C6 supports ATX PSUs (Corsair CX650 will fit)
- **Cooler**: ✅ Arctic Alpine 17 is low-profile (47mm), suitable for compact case
- **Power**: ✅ 650W is more than sufficient for this ~75W system

### Jonsbo C6 Dimensions
- **Size**: 315mm × 200mm × 315mm (H×W×D)
- **vs Previous Case**: ✓ Smaller than Sharkoon VS4-S (445×200×430mm)
- **2.5" Drive Bays**: 4 (perfect for your 4× SSDs)

## Existing Components Used

| Component | Model | Status |
|-----------|-------|--------|
| PSU | Corsair CX650 (ATX, 140mm) | ✅ Reusing |
| RAM | DDR4 (salvaged) | ✅ Reusing |
| Storage | 4× 480GB 2.5" SSDs | ✅ Reusing (ZFS array) |

## Alternative Options

### CPU Alternatives

| Option | Price | Notes |
|--------|-------|-------|
| Intel Core i5-14400F (Tray) | ₪750 | -₪245 - Same cores but **NO iGPU** (not recommended for Frigate) |
| Intel Core i5-12400 (Tray) | ₪845 | -₪150 - Previous gen, 6 cores, has iGPU |
| Intel Core i7-14700F (Tray) | ₪1,250 | +₪255 - 20 cores (8P+12E), overkill for this use case, no iGPU |

**Recommendation**: The i5-14400 is the sweet spot - 10 cores handle Docker workloads well, and the iGPU is essential for Frigate hardware transcoding.

### Motherboard Alternatives

| Option | Price | Notes |
|--------|-------|-------|
| MAXSUN Challenger H610M-H WIFI5 | ₪399 | -₪40 - Cheaper, includes WiFi, but H610 has fewer features |
| Gigabyte B760M GAMING DDR4 | ₪480 | +₪41 - Better VRMs, 2.5G LAN built-in (eliminates need for PCIe card) |

**Note**: If you choose Gigabyte B760M GAMING DDR4 (₪480), it has 2.5G LAN built-in, saving ₪79 on the network card. Net cost difference: -₪38.

### Case Alternatives

| Option | Price | Dimensions | Notes |
|--------|-------|------------|-------|
| FSP CMT195A | ₪205 | ~420×195×380mm | -₪60 - Budget option, may be larger |
| Jonsbo D300 | ₪450 | ~340×220×480mm | +₪185 - Premium, but exceeds width constraint |
| Lian Li O11 DYNAMIC MINI V2 | ₪390 | 380×170×288mm | +₪125 - Very compact, premium quality |

## Optimized Alternative Build

If you want to simplify with built-in 2.5G LAN:

| Component | Product | Price (ILS) |
|-----------|---------|-------------|
| CPU | Intel Core i5-14400 (Tray) | ₪995 |
| Motherboard | Gigabyte B760M GAMING DDR4 (has 2.5G LAN) | ₪480 |
| CPU Cooler | Arctic Alpine 17 CO | ₪55 |
| Case | Jonsbo C6 White | ₪265 |

**Total: ₪1,795** (saves ₪38 vs main build, one fewer component to install)

## Notes

### Frigate Considerations
- The Intel i5-14400's UHD 730 iGPU supports Quick Sync (hardware video decode/encode)
- For 3 cameras, Quick Sync can handle multiple 1080p/4K streams efficiently
- The 10 cores (6P+4E) provide plenty of headroom for detection models alongside transcoding
- This significantly reduces CPU load compared to software decoding

### Future Upgrades
- The B760 platform supports up to i9-14900 if you need more power later
- DDR4 is end-of-life but still performant for server workloads
- Case has room for additional storage if needed

### TP-Link Network Card
- If your existing TP-Link card is 2.5G or faster, you can skip the Cudy PE25 (save ₪79)
- Check the model number to confirm speed

### Power Consumption
- Estimated idle: ~30-40W
- Estimated load: ~75-100W
- The CX650 is significantly oversized, which is fine for efficiency and reliability
