export interface WebAnnouncementInfo {
    uid: string,
    title: string,
    release_time: number,
    pin_to_top: boolean,
}

export interface WebAnnouncementContent extends WebAnnouncementInfo {
    content: string,
    publisher: string,
    files?: Array<string>,
}