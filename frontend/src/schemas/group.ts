export interface Group {
  map(arg0: (item: any) => import("react/jsx-runtime").JSX.Element): any;
  id: number,
  name: string,
  number_of_members: number,
  members: Array<string>
}