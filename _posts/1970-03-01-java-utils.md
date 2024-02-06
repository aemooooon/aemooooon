---
layout: post
subtitle: Tools
categories: [Java]
header:
    image: header.jpg
    align:
    text: light
---

Java utils small static method collections.

```java
    /**
     * 工具集
     *
     * @author Hua Wang
     */
public class Utils {

    /**
     * 转换IPV4地址为整数
     *
     * @param ip IP地址 例： 113.24.9.27
     * @return 一个整数 例： 2130706433
     */
    public static Long ipV4ToLong(String ip) {
        String[] ips = ip.split("\\.");
        return (Long.parseLong(ips[0]) << 24) + (Long.parseLong(ips[1]) << 16) + (Long.parseLong(ips[2]) << 8) + Long.parseLong(ips[3]);
    }

    /**
     * 转换整数为IPV4地址
     *
     * @param ip 一个整数 例： 2130706433
     * @return IP地址 例： 113.24.9.27
     */
    public static String longToIpV4(Long ip) {
        AtomicReference<StringBuilder> sb = new AtomicReference<>(new StringBuilder());
        sb.get().append(ip >> 24)
                .append(".")
                .append((ip & 0x00FFFFFF) >> 16)
                .append(".")
                .append((ip & 0x0000FFFF) >> 8)
                .append(".")
                .append(ip & 0x000000FF);
        return sb.toString();
    }

```