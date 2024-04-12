import { ListItem } from  "../schemas/weblist"; 
  
  
export async function listData(): Promise<Array<ListItem>>{
  return Promise.resolve([
    {
      title: "1-1 第一題題意",
      creationDate: "2024年2月14日",
      poster: "Admin", 
    },
    {
      title: "1-1第二題",
      creationDate: "2024年2月12日",
      poster: "Admin", 
    },
    {
      title: "救我啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
      creationDate: "2024年2月9日",
      poster: "Admin", 
    },
  ]);
}