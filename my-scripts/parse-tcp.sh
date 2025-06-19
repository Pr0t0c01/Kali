#!/bin/bash

printf "%-30s %-30s %-15s\n" "Local Address" "Remote Address" "State"
echo "==============================================================================================="

while read -r line; do
    if [[ "$line" =~ ^sl ]]; then
        continue
    fi

    local_ip=$(echo "$line" | awk '{print $2}' | cut -d':' -f1)
    local_port=$(echo "$line" | awk '{print $2}' | cut -d':' -f2)
    remote_ip=$(echo "$line" | awk '{print $3}' | cut -d':' -f1)
    remote_port=$(echo "$line" | awk '{print $3}' | cut -d':' -f2)
    state=$(echo "$line" | awk '{print $4}')

    local_ip=$(echo "$local_ip" | sed 's/../& /g' | awk '{print $4"."$3"."$2"."$1}')
    remote_ip=$(echo "$remote_ip" | sed 's/../& /g' | awk '{print $4"."$3"."$2"."$1}')

    local_port=$((16#$local_port))
    remote_port=$((16#$remote_port))

    case "$state" in
        01) state="ESTABLISHED" ;;
        02) state="SYN_SENT" ;;
        03) state="SYN_RECV" ;;
        04) state="FIN_WAIT1" ;;
        05) state="FIN_WAIT2" ;;
        06) state="TIME_WAIT" ;;
        07) state="CLOSE" ;;
        08) state="CLOSE_WAIT" ;;
        09) state="LAST_ACK" ;;
        0A) state="LISTEN" ;;
        0B) state="CLOSING" ;;
        *) state="UNKNOWN" ;;
    esac

    printf "%-30s %-30s %-15s\n" "$local_ip:$local_port" "$remote_ip:$remote_port" "$state"
done < tcp
