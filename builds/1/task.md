# Spec

I had a home server that was used for running Home Assistant and several other workloads, mostly in Docker, that stopped working. I initially suspected a PSU failure and bought a new one, but it was ultimately a motherboard failure. 

I need to spec out a new build that will include the missing components: a motherboard, new CPU, CPU cooler, and case. I also have a TP-Link networking card. Other requirements include Ethernet ports supporting at least 2.5G and a case that is as compact as possible—specifically smaller than my previous case, the Sharkoon VS4-S (445mm x 200mmx430mm)

# Run Requirements 

- Docker workloads 
- Frigate (3 cams)

# Existing Components

| PSU | Corsair CX650 (ATX, 140mm) | ✓ Use |
| RAM | DDR4 (salvaged) | ✓ Use |
| Storage | 4× 480GB 2.5" SSDs | ✓ Use (ZFS array) |

# Task

Generate a suggested spec in suggested-build.md