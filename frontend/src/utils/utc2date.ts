export default function UTC2Date(timestamp: number): Date {
    const offset = (new Date()).getTimezoneOffset() * 60;
    timestamp -= offset;
    timestamp *= 1000;
    return (new Date(timestamp));
};
