# Research Questions (RQs)

## Internet of Vehicles and V2X

### RQ1: How do C-V2X and IEEE 802.11p/bd compare technically, and what is the current state of deployment?

#### Reference Papers (RPs):
1. **[RP1] Nurkahfi et al. (2024):** G. N. Nurkahfi et al., *"On SDN to Support the IEEE 802.11 and C-V2X-Based Vehicular Communications Use-Cases and Performance: A Comprehensive Survey,"* IEEE Access, vol. 12, pp. 33410-33492, 2024. ([accessible](https://ieeexplore.ieee.org/document/10352136))
2. **[RP2] Anwar et al. (2019):** W. Anwar, N. Franchi, and G. Fettweis, *"Physical Layer Evaluation of V2X Communications Technologies: 5G NR-V2X, LTE-V2X, IEEE 802.11bd, and IEEE 802.11p,"* in Proc. IEEE 90th Vehicular Technology Conference (VTC-Fall), 2019, pp. 1-7. ([accessible](https://ieeexplore.ieee.org/document/8891313))
3. **[RP3] Hejazi & Bokor (2022):** H. Hejazi and L. Bokor, *"A Survey on the Use-Cases and Deployment Efforts Toward Converged Internet of Things (IoT) and Vehicle-to-Everything (V2X) Environments,"* Acta Technica Jaurinensis, vol. 15, no. 2, pp. 58-73, 2022. ([accessible](https://acta.sze.hu/index.php/acta/article/view/627))

---

### 1. Introduction

* **RAT Families & Governance:** Vehicular communications are enabled mainly by two major **Radio Access Technology (RAT)** families [RP1, RP2, RP3]:
  * **Wi-Fi-based Family:** Standardized by the **IEEE** (Institute of Electrical and Electronics Engineers) and **ETSI** (European Telecommunications Standards Institute).
  * **Cellular-based Family (C-V2X):** Standardized globally by the **3GPP** (3rd Generation Partnership Project).

* **Regional Frameworks [RP1, RP3]:**
  * **United States:** Wi-Fi vehicular technology is designated as **DSRC** (Dedicated Short-Range Communications) operating under the **WAVE** (Wireless Access in Vehicular Environments) architecture. WAVE uses **IEEE 802.11p** for the Physical (PHY) and Data Link (MAC) layers, supported by the **IEEE 1609** standards suite for transport, network, and security. DSRC features low end-to-end latency, low cost, and decentralized ad-hoc flexibility without requiring central infrastructure. Disadvantages include line-of-sight (LOS) occlusions and poor scalability under high channel loads. Recent **FCC** regulatory spectrum allocations have accelerated a shift toward **C-V2X**.
  * **Europe:** Wi-Fi vehicular communications operate under **C-ITS** (Cooperative Intelligent Transport Systems) or **ITS-G5** (ETSI EN 302 663), utilizing IEEE 802.11p as the access layer.
  * **Cellular V2X (C-V2X):** Encompasses **LTE-V2X** (3GPP Rel. 14/15) and **5G NR-V2X** (3GPP Rel. 16+). Operating via direct **PC5 Sidelink** (5.9 GHz) and cellular **Uu** interfaces, cellular networks offer wide coverage, robust security, high throughput, and superior scalability, though requiring centralized management and infrastructure investments.

* **Evolution Timeline:** IEEE 802.11p was standardized in 2010, whereas LTE-V2X emerged in 2015–2016, followed by IEEE 802.11bd (2022) and 5G NR-V2X (2020+) [RP1, RP2].

---

### 2. Problem & Multi-RAT Coexistence

* **Spectrum Scarcity:** Operating strictly within a single RAT family cannot meet all vehicular safety demands under varying traffic densities in the shared **5.9 GHz ITS band** [RP1 / Ref. 38 - Bazzi et al., 2022].

* **Density & Operational Adaptation:**
  * **IEEE 802.11p** is well-suited for low-to-moderate vehicle density scenarios, whereas **LTE-V2X** and **5G NR-V2X** excel in dense urban traffic [RP1 / Ref. 36 - Ansari, 2021].
  * Coexistence of multiple RATs addresses multi-hop V2X limitations, high latency, and low data rates [RP1 / Ref. 6 - Qi et al., 2020].

* **Coexistence Mechanisms:**
  * **Fixed Preamble Insertion:** Inserting an IEEE 802.11p preamble into LTE-V2X frames reduces co-channel collisions in dense traffic [RP1 / Ref. 38 - Bazzi et al., 2022].
  * **Vehicle Clustering & Smart Routing:** Grouping vehicles into dynamic clusters to select between cellular and DSRC based on network metrics improves **Quality of Service (QoS)**, reduces overall network load, and minimizes unnecessary handovers [RP1 / Ref. 6 - Qi et al., 2020].
  * **Software-Defined Networking (SDN):** SDN-based control plane management orchestrates hybrid protocol stacks, creating fewer vertical handovers, higher link reliability, and reduced transmission delays [RP1 / Ref. 40 - Mir et al., 2020].

---

### 3. Technical Performance Comparison & Specifications

*(Data sources: Physical layer simulations and analytical models from **RP2 (Anwar et al., 2019)**, survey synthesis from **RP1 (Nurkahfi et al., 2024)**, and 3GPP/IEEE standards specifications)*

| Technical Parameter | IEEE 802.11p (DSRC / ITS-G5) | IEEE 802.11bd (Next-Gen Wi-Fi) | LTE-V2X (C-V2X Rel. 14/15) | 5G NR-V2X (C-V2X Rel. 16+) |
| :--- | :--- | :--- | :--- | :--- |
| **Standardization Body** | IEEE (2010) / ETSI Rel. 1 | IEEE (802.11bd-2022) / ETSI Rel. 2 | 3GPP Rel. 14/15 (2017) | 3GPP Rel. 16+ (2020) |
| **Operating Frequency** | 5.855 – 5.925 GHz | 5.9 GHz ITS band & 6 GHz | 5.9 GHz ITS & Cellular Bands | 5.9 GHz, sub-6 GHz (FR1), mmWave (FR2) |
| **Channel Bandwidth** | **10 MHz** (optional 20 MHz) | **10 MHz, 20 MHz** (Bonding to 40 MHz) | **10 MHz, 20 MHz** | **10–100 MHz** (FR1) / **400 MHz** (FR2) |
| **Peak Data Rate** | **3 – 27 Mbps** (Default: **6 Mbps**) | **54 – 108 Mbps+** | **26 – 50 Mbps** (PC5 Sidelink) | **Up to 1 Gbps+** (Sidelink Mode 2 / Uu) |
| **Latency (End-to-End)** | **< 10 ms** (PHY ~1–2 ms) | **< 5 ms** | **< 20 ms** (Sidelink Mode 4) | **< 1 – 3 ms** (URLLC mini-slots) |
| **Effective Range** | **~300 m – 500 m** | **~1000 m+** (DCM & Midambles) | **~450 m – 1000 m** | **> 1000 m+** (Direct Sidelink & Uu) |
| **Subcarrier Spacing (SCS)** | **156.25 kHz** (OFDM) | **156.25 kHz / 312.5 kHz** | **15 kHz** (SC-FDMA / OFDM) | Flexible **15, 30, 60 kHz** (FR1) / **120, 240 kHz** (FR2) |
| **Channel Coding** | Convolutional Coding | LDPC | Turbo Coding | LDPC (Data) / Polar (Control) |
| **Target Use Cases** | Basic Safety Beacons (CAM/BSM) | High-speed safety, Extended Range | Basic & Enhanced Safety, Platooning | URLLC, Cooperative Perception, Remote Driving |

---

### 4. Paper Results & Empirical Findings

#### 4.1 SDN Survey Synthesis – Performance Comparison of Vehicular RATs [RP1 / Nurkahfi et al. Table 2]

1. **[RP2 / RP1 - Ref. 23 (Anwar et al., 2019)]** 5G NR-V2X outperformed IEEE 802.11bd, and IEEE 802.11bd outperformed IEEE 802.11p regarding latency and data rates. IEEE 802.11bd improves the performance of IEEE 802.11p in high Doppler scenarios. Dual Carrier Modulation (DCM) and Range Extension (RE) options in IEEE 802.11bd improve cell-edge performance and communication range.
2. **[RP1 - Ref. 5 (Nguyen et al., 2017)]** LTE-V2X communication range and Packet Delivery Ratio (PDR) are superior to IEEE 802.11p in highway scenarios.
3. **[RP1 - Ref. 21 (Ma et al., 2021)]** Safety communication performance requirements can be met by IEEE 802.11bd, whereas IEEE 802.11p fails under stringent multi-layer QoS conditions.
4. **[RP1 - Ref. 30 (Benkirane & Benaziz, 2018)]** IEEE 802.16e exhibits a lower packet drop rate than IEEE 802.11p across speeds. Communication throughput for IEEE 802.11p is superior below 90 km/h; above 90 km/h, IEEE 802.16e performs better.
5. **[RP1 - Ref. 22 (Jacob et al., 2020)]** Packet Reception Ratio (PRR) of IEEE 802.11bd (with or without DCM+RE) exceeds IEEE 802.11p. While DCM+RE extends communication range, extended coverage can induce channel congestion.
6. **[RP1 - Ref. 25 (Mir & Filali, 2014)]** LTE-V2X outperforms IEEE 802.11p in terms of beaconing frequency, vehicle mobility support, and scalability.
7. **[RP1 - Ref. 31 (Vinel, 2012)]** IEEE 802.11p supports beacon message transmission for basic safety applications better than legacy LTE.
8. **[RP1 - Ref. 32 (Yacheur et al., 2020)]** IEEE 802.11bd delivers higher throughput and lower latency than IEEE 802.11p, with a superior PRR (88% vs. 75%).
9. **[RP1 - Ref. 33 (Ma & Trivedi, 2021)]** IEEE 802.11bd fulfills SINR-based QoS requirements across PHY, MAC, and Application layers for advanced safety applications that IEEE 802.11p cannot fulfill.
10. **[RP1 - Ref. 34 (Ehsanfar et al., 2022)]** Unique Word (UW)-based PHY with low-complexity channel estimation matches the performance of high-complexity estimation in the IEEE 802.11bd standard draft.
11. **[RP1 - Ref. 35 (Triwinarko et al., 2021)]** IEEE 802.11bd PHY layer enhancements surpass IEEE 802.11p in high Doppler scenarios and extends communication range.
12. **[RP1 - Ref. 16 (Molina-Masegosa et al., 2020)]** IEEE 802.11p handles variations in message size and generation intervals better than LTE-V2X. However, under shallow channel load conditions, IEEE 802.11p incurs higher operational inefficiency than LTE-V2X.

#### 4.2 SDN Survey Synthesis – RAT Coexistence [RP1 / Nurkahfi et al. Table 3]

1. **[RP1 - Ref. 6 (Qi et al., 2020)]** Implementing vehicle clustering and dynamic RAT selection improves communication QoS while reducing network load and vertical handovers.
2. **[RP1 - Ref. 38 (Bazzi et al., 2022)]** Coexistence methods using fixed preambles successfully reduce collisions between RATs in high vehicle density conditions.
3. **[RP1 - Ref. 36 (Ansari, 2021)]** IEEE 802.11p meets safety performance requirements in low-to-moderate vehicle density, while LTE-V2X meets requirements in high density conditions.
4. **[RP1 - Ref. 39 (Ghafoor et al., 2020)]** The QoS-Aware Relaying (QR) algorithm successfully mitigates error-prone wireless channel conditions.
5. **[RP1 - Ref. 40 (Mir et al., 2020)]** Implementing an SDN protocol stack for hybrid vehicular RATs results in fewer vertical handovers, higher reliability, and lower transmission delays.

#### 4.3 SDN Survey – Figure 3: Illustration of Multi-RAT Implementation [RP1]

![Multi-RAT Implementation](figure3_multi_Rat_implementation_example.png)

---

### 5. Global Deployment Efforts & Field Trials [RP3 / Hejazi & Bokor, 2022, Sec. V]

#### 5.1 Europe (C-ITS / ITS-G5 & Hybrid Networks)

* **C-ROADS Platform:** Operational across 43 cities in 16 European countries. Standardizes C-ITS "Day-1" safety services (hazardous location warnings, roadworks alerts) using **Roadside Units (RSUs)**, **On-Board Units (OBUs)**, and **AMQP** back-office message brokers.
* **CROCODILE / CROCODILE 2:** Encompasses 13 Central and Eastern European countries across 15 border crossings, leveraging CCTV, roadside sensors, and National Access Points (NAPs) for cross-border traffic management.
* **NordicWay (1, 2, & 3):** Multi-country pilot (Denmark, Finland, Norway, Sweden) demonstrating cloud-to-cloud hybrid cellular C-ITS communications for automated driving (CCAM).
* **SCOOP@F:** Connected 3,000 vehicles across 2,000 km of French highways, transitioning from pure ITS-G5 Wi-Fi to hybrid cellular communications.
* **AUTOPILOT & InterCor:** Validated automated car-sharing, automated valet parking, and cross-border corridor interoperability using IoT platforms and multi-RAT communications.

#### 5.2 United States (DSRC Pilots to C-V2X Transition)

* **NYCDOT Connected Vehicle Pilot:** Deployed 353 RSUs and 8,000 equipped vehicles in New York City advancing *Vision Zero* safety goals using DSRC at 5.9 GHz.
* **Tampa DOT Pilot (THEA):** Installed 47 RSUs and ~1,000 OBUs in Florida, integrating 12 V2V, V2I, and V2P safety applications connected to a Traffic Management Center (TMC).
* **Wyoming DOT Pilot (WYDOT):** Equipped 75 RSUs and 400 commercial freight trucks along the I-80 corridor for real-time weather and collision warnings.
* **C-V2X Transition:** Following FCC regulatory spectrum reallocations, US deployments are actively transitioning toward cellular C-V2X direct communications.

#### 5.3 Asia & Australasia

* **China (Wuxi C-V2X Project):** City-scale C-V2X deployment in Wuxi led by Huawei, deploying C-V2X RSUs and smart traffic infrastructure as a global benchmark.
* **South Korea (MOLIT):** National C-ITS deployment program managed by the Ministry of Land, Infrastructure, and Transport.
* **Japan & Australasia:** Japan deployed C-ITS across its highway system; Australia and New Zealand advance regional pilots through the **Austroads** initiative.

#### 5.4 Required Infrastructure & Capital Investment

* **Roadside Infrastructure:** Installation of **RSUs**, traffic signal controllers, sensors (cameras/LiDAR), and high-speed fiber backhaul.
* **Vehicular Hardware:** **OBUs**, dual-mode radio modems (Wi-Fi/Cellular), and **Hardware Security Modules (HSMs)** for cryptographic signature processing.
* **Network & Compute Nodes:** **Multi-access Edge Computing (MEC)** servers at base stations/RSUs for low-latency spatial data fusion, Traffic Management Centers (TMCs), and **Vehicular Public Key Infrastructure (VPKI)** backend servers for pseudonym credential management.