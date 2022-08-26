---
layout: post
title:  "jetson-xavier-nx设备树"
date:   2022-08-26 17:36:26 +0800
categories: jekyll update
---

### dtb文件反编译
https://blog.csdn.net/huiyuanliyan/article/details/119978131

### 修改设备树，识别底板上的sd卡
一共修改4个文件，具体步骤如下   
- [获取内核源码](https://docs.nvidia.com/jetson/archives/r34.1/DeveloperGuide/text/SD/Kernel/KernelCustomization.html#manually-downloading-and-expanding-kernel-sources)
- `tegra194-p3668-common.dtsi`,在`sdhci_sd`后增加
```
	sdhci_sdcard: sdhci@3440000 {
		mmc-ocr-mask = <0x0>;
		cd-inverted;
		cd-gpios = <&tegra_main_gpio TEGRA194_MAIN_GPIO(Q, 6) 0>;
		nvidia,cd-wakeup-capable;
		mmc-ocr-mask = <0>;
		cd-inverted;
		vmmc-supply = <&p3668_vdd_sdmmc3_sw>;
		nvidia,vmmc-always-on;
		status = "okay";
	};
```
- `tegra194-soc-sdhci.dtsi`,`sdmmc3: sdhci@3440000`中`status = "disabled"`;改为`status = "okay"`;
- `tegra194-power-tree-p3668.dtsi`，在`sdhci@3400000`后增加
```
	sdhci@3440000 {
		vmmc-supply = <&p3668_vdd_sdmmc1_sw>;
	};
```
- `tegra194-fixed-regulator-p3668.dtsi`,在`p3668_vdd_sdmmc1_sw`后增加
```
		p3668_vdd_sdmmc3_sw: regulator@106 {
			compatible = "regulator-fixed";
			reg = <106>;
			regulator-name = "vdd-sdmmc3-sw";
			regulator-min-microvolt = <3300000>;
			regulator-max-microvolt = <3300000>;
			gpio = <&tegra_main_gpio TEGRA194_MAIN_GPIO(Q, 1) 0>;
			regulator-always-on;
			enable-active-high;
		};
```